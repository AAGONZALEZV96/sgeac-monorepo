import os
import boto3

def get_dynamodb_client():
    """Crea y devuelve un cliente de DynamoDB configurado para LocalStack si es necesario."""
    if os.environ.get('IS_OFFLINE'):
        return boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
    return boto3.client("dynamodb")

def deserialize_item(item):
    """Convierte un item de DynamoDB a dict de Python."""
    if not item:
        return None
    result = {}
    for key, val in item.items():
        typ = list(val.keys())[0]
        result[key] = val[typ]
    return result
