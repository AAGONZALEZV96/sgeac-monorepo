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
    return {key: list(val.values())[0] for key, val in item.items()}

def handler(event, context):
    tipo_nivel_id = event['pathParameters']['id']
    response = dynamodb_client.get_item(TableName=TABLE_NAME, Key={'id': {'S': tipo_nivel_id}})
    
    if 'Item' in response:
        item = deserialize_item(response['Item'])
        return {"statusCode": 200, "body": json.dumps(item)}
    else:
        return {"statusCode": 404, "body": json.dumps({"error": "Tipo de Nivel no encontrado."})}