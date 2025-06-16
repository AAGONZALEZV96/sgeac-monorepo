import os
import json
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def deserialize_item(item):
    """
    Convierte un item de formato DynamoDB a un diccionario de Python.
    Maneja correctamente los tipos String (S) y Number (N).
    """
    deserialized = {}
    for key, val_dict in item.items():
        val_type = list(val_dict.keys())[0]
        value = val_dict[val_type]
        if val_type == 'N':
            deserialized[key] = int(value)
        else:
            deserialized[key] = value
    return deserialized

def handler(event, context):
    """
    Handler para escanear y devolver todos los niveles.
    """
    try:
        response = dynamodb_client.scan(TableName=TABLE_NAME)
        items = [deserialize_item(item) for item in response.get('Items', [])]
        return {
            "statusCode": 200,
            "body": json.dumps(items)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno del servidor: {str(e)}"})
        }