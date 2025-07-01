import os
import json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
USERS_TABLE   = os.environ['DYNAMODB_TABLE']
NIVELES_TABLE = os.environ.get(
    'NIVELES_TABLE',
    f"sgeac-niveles-table-{os.environ.get('STAGE','local')}"
)

def handler(event, context):
    try:
        user_id  = event['pathParameters']['id']
        body     = json.loads(event.get("body", "{}"))
        nivel_id = body.get('nivel_id')

        # --- Validación básica ---
        if nivel_id is None:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "El 'nivel_id' es requerido (cadena vacía para desasignar)."
                })
            }

        # --- Leer usuario actual ---
        resp_user = DYNAMODB_CLIENT.get_item(
            TableName=USERS_TABLE,
            Key={'id': {'S': user_id}}
        )
        user = resp_user.get('Item')
        if not user:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Usuario no encontrado."})
            }
        current_nivel = user.get('nivel_actual_id', {}).get('S')

        # --- Desasignar nivel (nivel_id == "") ---
        if nivel_id == "":
            # Si no tenía nivel, nada que hacer
            if not current_nivel:
                return {
                    "statusCode": 200,
                    "body": json.dumps({"message": "Usuario ya sin nivel asignado."})
                }
            # Decrementar cupos en nivel viejo
            DYNAMODB_CLIENT.update_item(
                TableName=NIVELES_TABLE,
                Key={'id': {'S': current_nivel}},
                UpdateExpression="SET cupos_actuales = cupos_actuales - :dec",
                ExpressionAttributeValues={":dec": {"N": "1"}}
            )
            # Quitar atributos nivel_actual_id y clase
            DYNAMODB_CLIENT.update_item(
                TableName=USERS_TABLE,
                Key={'id': {'S': user_id}},
                UpdateExpression="REMOVE nivel_actual_id, clase",
                ReturnValues="ALL_NEW"
            )
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Alumno desasignado de la clase."})
            }

        # --- Asignar a nuevo nivel ---
        # 1) Obtener nivel y validar existencia
        resp_nivel = DYNAMODB_CLIENT.get_item(
            TableName=NIVELES_TABLE,
            Key={'id': {'S': nivel_id}}
        )
        nivel = resp_nivel.get('Item')
        if not nivel:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Nivel especificado no existe."})
            }
        cupos_actuales = int(nivel['cupos_actuales']['N'])
        cupos_maximos  = int(nivel['cupos_maximos']['N'])
        tipo_nivel_id  = nivel['tipo_nivel_id']['S']

        # 2) Validar cupos disponibles
        if cupos_actuales >= cupos_maximos:
            return {
                "statusCode": 409,
                "body": json.dumps({"error": "Cupos completos en el nivel seleccionado."})
            }

        # 3) Si ya estaba en otro nivel, decrementarlo
        if current_nivel:
            DYNAMODB_CLIENT.update_item(
                TableName=NIVELES_TABLE,
                Key={'id': {'S': current_nivel}},
                UpdateExpression="SET cupos_actuales = cupos_actuales - :dec",
                ExpressionAttributeValues={":dec": {"N": "1"}}
            )

        # 4) Incrementar cupos del nuevo nivel
        DYNAMODB_CLIENT.update_item(
            TableName=NIVELES_TABLE,
            Key={'id': {'S': nivel_id}},
            UpdateExpression="SET cupos_actuales = cupos_actuales + :inc",
            ExpressionAttributeValues={":inc": {"N": "1"}}
        )

        # 5) Actualizar usuario: nivel_actual_id + clase = tipo_nivel_id
        DYNAMODB_CLIENT.update_item(
            TableName=USERS_TABLE,
            Key={'id': {'S': user_id}},
            UpdateExpression="SET nivel_actual_id = :nid, clase = :clase",
            ExpressionAttributeValues={
                ":nid":   {"S": nivel_id},
                ":clase": {"S": tipo_nivel_id},
            },
            ReturnValues="ALL_NEW"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Alumno asignado al nivel exitosamente."})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno: {str(e)}"})
        }
