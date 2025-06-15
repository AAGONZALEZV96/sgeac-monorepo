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

def handler(event, context):
    """
    Handler para eliminar un usuario por su ID.
    """
    try:
        # Extraer el ID de la URL
        user_id = event['pathParameters']['id']

        # Eliminar el item de DynamoDB
        dynamodb_client.delete_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': user_id}}
        )

        logger.info(f"Usuario eliminado con ID: {user_id}")
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Usuario eliminado exitosamente."})
        }

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Ocurrió un error interno al eliminar el usuario."})
        }