import os
import json
import boto3
import logging

# Configuración idéntica al otro archivo
logger = logging.getLogger()
logger.setLevel(logging.INFO)

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client(
        "dynamodb", endpoint_url="http://localhost.localstack.cloud:4566"
    )
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    """
    Handler para obtener un usuario por su ID.
    El ID se extrae de los parámetros de la ruta de la URL.
    """
    try:
        # Extraer el ID del usuario de los pathParameters
        user_id = event['pathParameters']['id']
        logger.info(f"Buscando usuario con ID: {user_id}")

        # Buscar el item en DynamoDB usando la clave primaria 'id'
        response = dynamodb_client.get_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': user_id}}
        )

        # Verificar si se encontró el item
        if 'Item' in response:
            item = response['Item']
            
            # Convertir el formato de DynamoDB a un JSON limpio y legible
            user_data = {
                'id': item['id']['S'],
                'rut': item['rut']['S'],
                'nombre': item['nombre']['S'],
                'email': item['email']['S'],
                'edad': int(item['edad']['N']),
                'rol': item['rol']['S'],
                'sucursal': item['sucursal']['S']
            }

            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(user_data)
            }
        else:
            # Si no hay 'Item' en la respuesta, el usuario no fue encontrado
            logger.warning(f"Usuario no encontrado con ID: {user_id}")
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Usuario no encontrado."})
            }

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Ocurrió un error interno en el servidor."})
        }