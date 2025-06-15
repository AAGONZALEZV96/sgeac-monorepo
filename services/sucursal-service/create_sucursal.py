import os
import json
import uuid  # Importamos la librería para generar IDs aleatorios
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

def handler(event, context):
    """
    Crea una nueva sucursal con un ID aleatorio (UUID).
    """
    try:
        data = json.loads(event.get("body", "{}"))

        # Generar un ID único y aleatorio
        sucursal_id = str(uuid.uuid4())
        
        # Atributos de la sucursal
        item = {
            'id': {'S': sucursal_id},
            'nombre': {'S': data.get('nombre')},
            'direccion': {'S': data.get('direccion')},
            'telefono': {'S': data.get('telefono')},
            'correo_contacto': {'S': data.get('correo_contacto')},
            'comuna': {'S': data.get('comuna')}
        }

        # Guardar en DynamoDB
        dynamodb_client.put_item(
            TableName=TABLE_NAME,
            Item=item
        )
        
        logger.info(f"Sucursal creada con ID: {sucursal_id}")

        # Devolvemos el item completo que fue creado
        response_body = {key: val['S'] for key, val in item.items()}

        return {
            "statusCode": 201,
            "body": json.dumps(response_body)
        }

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Ocurrió un error interno al crear la sucursal."})
        }