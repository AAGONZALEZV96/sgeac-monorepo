import os
import json
import boto3
import logging

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

def deserialize_item(item):
    """
    Convierte un item de formato DynamoDB a un diccionario de Python normal.
    """
    deserialized = {
        'id': item['id']['S'],
        'rut': item['rut']['S'],
        'nombre': item['nombre']['S'],
        'email': item['email']['S'],
        'edad': int(item['edad']['N']),
        'rol': item['rol']['S'],
        'sucursal': item['sucursal']['S']
    }
    return deserialized

def handler(event, context):
    """
    Handler para escanear y devolver todos los usuarios de la tabla.
    """
    try:
        # Usamos la operación 'scan' para leer todos los items de la tabla
        response = dynamodb_client.scan(TableName=TABLE_NAME)
        
        # 'scan' devuelve los items bajo la clave 'Items'
        items = response.get('Items', [])

        # Deserializamos cada item para devolver un JSON limpio
        deserialized_items = [deserialize_item(item) for item in items]

        logger.info(f"Se encontraron {len(deserialized_items)} usuarios.")
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(deserialized_items)
        }

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Ocurrió un error interno al listar los usuarios."})
        }