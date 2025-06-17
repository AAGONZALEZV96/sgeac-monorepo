import os, json
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
USERS_TABLE = os.environ['DYNAMODB_TABLE']
NIVELES_TABLE_NAME = f"sgeac-niveles-table-{os.environ.get('STAGE', 'local')}"

def handler(event, context):
    try:
        user_id = event['pathParameters']['id']
        body = json.loads(event.get("body", "{}"))
        nivel_id = body.get('nivel_id')

        if not nivel_id:
            return {"statusCode": 400, "body": json.dumps({"error": "El 'nivel_id' es requerido."})}

        response_nivel = DYNAMODB_CLIENT.get_item(
            TableName=NIVELES_TABLE_NAME, Key={'id': {'S': nivel_id}}
        )
        if 'Item' not in response_nivel:
            return {"statusCode": 404, "body": json.dumps({"error": "El Nivel especificado no existe."})}
        
        nivel = response_nivel['Item']
        cupos_actuales = int(nivel['cupos_actuales']['N'])
        cupos_maximos = int(nivel['cupos_maximos']['N'])

        if cupos_actuales >= cupos_maximos:
            return {
                "statusCode": 409,
                "body": json.dumps({"message": "Cupos completos en nivel seleccionado, consultar en sucursal mas cercana o enviar email a contacto@academia.com"})
            }

        DYNAMODB_CLIENT.update_item(
            TableName=NIVELES_TABLE_NAME,
            Key={'id': {'S': nivel_id}},
            UpdateExpression="SET cupos_actuales = cupos_actuales + :inc",
            ExpressionAttributeValues={":inc": {"N": "1"}}
        )

        DYNAMODB_CLIENT.update_item(
            TableName=USERS_TABLE,
            Key={'id': {'S': user_id}},
            UpdateExpression="SET nivel_actual_id = :nid",
            ExpressionAttributeValues={":nid": {"S": nivel_id}},
            ReturnValues="ALL_NEW"
        )

        return {"statusCode": 200, "body": json.dumps({"message": "Alumno asignado al nivel exitosamente."})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": f"Error interno: {str(e)}"}) }