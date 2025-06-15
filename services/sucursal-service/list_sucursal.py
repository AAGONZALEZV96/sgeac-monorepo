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
    """Convierte un item de formato DynamoDB a un diccionario de Python."""
    return {key: list(val.values())[0] for key, val in item.items()}

def handler(event, context):
    response = dynamodb_client.scan(TableName=TABLE_NAME)
    items = response.get('Items', [])
    deserialized_items = [deserialize_item(item) for item in items]
    return {
        "statusCode": 200,
        "body": json.dumps(deserialized_items)
    }