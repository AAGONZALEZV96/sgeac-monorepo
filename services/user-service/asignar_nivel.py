import os
import json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
USERS_TABLE       = os.environ['DYNAMODB_TABLE']
NIVELES_TABLE     = os.environ.get('NIVELES_TABLE', f"sgeac-niveles-table-{os.environ.get('STAGE','local')}")

def handler(event, context):
    try:
        user_id = event['pathParameters']['id']
        body = json.loads(event.get("body", "{}"))
        nivel_id = body.get('nivel_id')

        # Validación básica
        if nivel_id is None:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "El 'nivel_id' es requerido (puede ser cadena vacía para desasignar)."})
            }

        # 1) Leemos el usuario para saber su nivel actual (si existe)
        resp_user = DYNAMODB_CLIENT.get_item(
            TableName=USERS_TABLE,
            Key={'id': {'S': user_id}}
        )
        user = resp_user.get('Item')
        if not user:
            return {"statusCode": 404, "body": json.dumps({"error": "Usuario no encontrado."})}

        current_nivel = user.get('nivel_actual_id', {}).get('S')

        # 2) Si vienen con nivel_id == "" → desasignar:
        if nivel_id == "":
            # Si no tenía nivel, no hay nada que hacer
            if not current_nivel:
                return {"statusCode": 200, "body": json.dumps({"message": "Usuario ya sin nivel asignado."})}

            # Decrementar cupos en el nivel viejo
            DYNAMODB_CLIENT.update_item(
                TableName=NIVELES_TABLE,
                Key={'id': {'S': current_nivel}},
                UpdateExpression="SET cupos_actuales = cupos_actuales - :dec",
                ExpressionAttributeValues={":dec": {"N": "1"}}
            )
            # Quitar el atributo nivel_actual_id
            DYNAMODB_CLIENT.update_item(
                TableName=USERS_TABLE,
                Key={'id': {'S': user_id}},
                UpdateExpression="REMOVE nivel_actual_id",
                ReturnValues="ALL_NEW"
            )
            return {"statusCode": 200, "body": json.dumps({"message": "Alumno desasignado de su clase."})}

        # 3) Para asignar a un nuevo nivel → validar existencia y cupos
        resp_nivel = DYNAMODB_CLIENT.get_item(
            TableName=NIVELES_TABLE,
            Key={'id': {'S': nivel_id}}
        )
        nivel = resp_nivel.get('Item')
        if not nivel:
            return {"statusCode": 404, "body": json.dumps({"error": "Nivel especificado no existe."})}

        cupos_actuales = int(nivel['cupos_actuales']['N'])
        cupos_maximos  = int(nivel['cupos_maximos']['N'])
        if cupos_actuales >= cupos_maximos:
            return {
                "statusCode": 409,
                "body": json.dumps({
                    "error": "Cupos completos en el nivel seleccionado."
                })
            }

        # 4) Si el usuario ya estaba en otro nivel, primero desasignarlo de ahí
        if current_nivel:
            DYNAMODB_CLIENT.update_item(
                TableName=NIVELES_TABLE,
                Key={'id': {'S': current_nivel}},
                UpdateExpression="SET cupos_actuales = cupos_actuales - :dec",
                ExpressionAttributeValues={":dec": {"N": "1"}}
            )

        # 5) Incrementar cupos del nuevo nivel
        DYNAMODB_CLIENT.update_item(
            TableName=NIVELES_TABLE,
            Key={'id': {'S': nivel_id}},
            UpdateExpression="SET cupos_actuales = cupos_actuales + :inc",
            ExpressionAttributeValues={":inc": {"N": "1"}}
        )

        # 6) Actualizar al usuario con su nuevo nivel
        DYNAMODB_CLIENT.update_item(
            TableName=USERS_TABLE,
            Key={'id': {'S': user_id}},
            UpdateExpression="SET nivel_actual_id = :nid",
            ExpressionAttributeValues={":nid": {"S": nivel_id}},
            ReturnValues="ALL_NEW"
        )

        return {"statusCode": 200, "body": json.dumps({"message": "Alumno asignado al nivel exitosamente."})}

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno: {str(e)}"})
        }
