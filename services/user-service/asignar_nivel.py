# services/user-service/asignar_nivel.py

import os
import json
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

# Obtenemos los nombres de ambas tablas desde las variables de entorno
USERS_TABLE = os.environ['DYNAMODB_TABLE']
# ¡IMPORTANTE! Deberás añadir NIVELES_TABLE a las variables de entorno en serverless.yml
# Para simplificar por ahora, lo pondremos directamente en el código
NIVELES_TABLE_NAME = f"sgeac-niveles-table-{os.environ.get('STAGE', 'local')}"

def handler(event, context):
    try:
        user_id = event['pathParameters']['id']
        body = json.loads(event.get("body", "{}"))
        nivel_id = body.get('nivel_id')

        if not nivel_id:
            return {"statusCode": 400, "body": json.dumps({"error": "El 'nivel_id' es requerido."})}

        # --- PASO 1: Leer el Nivel y verificar los cupos ---
        response_nivel = dynamodb_client.get_item(
            TableName=NIVELES_TABLE_NAME, Key={'id': {'S': nivel_id}}
        )
        if 'Item' not in response_nivel:
            return {"statusCode": 404, "body": json.dumps({"error": "El Nivel especificado no existe."})}
        
        nivel = response_nivel['Item']
        cupos_actuales = int(nivel['cupos_actuales']['N'])
        cupos_maximos = int(nivel['cupos_maximos']['N'])

        if cupos_actuales >= cupos_maximos:
            # Tu mensaje de error personalizado
            return {
                "statusCode": 409, # 409 Conflict es un buen código para "no se puede por una regla de negocio"
                "body": json.dumps({"message": "Cupos completos en nivel seleccionado, consultar en sucursal mas cercana o enviar email a contacto@academia.com"})
            }

        # --- PASO 2: Si hay cupos, actualizar ambas tablas ---
        # (Nota: en un sistema de producción, esto se haría en una transacción para mayor seguridad)

        # 2a. Incrementar el contador de cupos en la tabla de Niveles
        dynamodb_client.update_item(
            TableName=NIVELES_TABLE_NAME,
            Key={'id': {'S': nivel_id}},
            UpdateExpression="SET cupos_actuales = cupos_actuales + :inc",
            ExpressionAttributeValues={":inc": {"N": "1"}}
        )

        # 2b. Asignar el nivel al usuario en la tabla de Usuarios
        response_user = dynamodb_client.update_item(
            TableName=USERS_TABLE,
            Key={'id': {'S': user_id}},
            UpdateExpression="SET nivel_actual_id = :nid",
            ExpressionAttributeValues={":nid": {"S": nivel_id}},
            ReturnValues="ALL_NEW"
        )

        return {"statusCode": 200, "body": json.dumps({"message": "Alumno asignado al nivel exitosamente."})}

    except Exception as e:
        # En caso de error, sería ideal revertir el incremento del cupo, pero por simplicidad lo omitimos.
        return {"statusCode": 500, "body": json.dumps({"error": f"Error interno: {str(e)}"}) }