# services/niveles-service/list_niveles_by_tipo.py
import os
import json
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

def deserialize_item(item):
    return {key: list(val.values())[0] for key, val in item.items()}

TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['TIPO_NIVEL_INDEX']

def handler(event, context):
    tipo_id = event['pathParameters']['tipo_id']
    
    # Usamos query en el índice en vez de scan en la tabla
    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        IndexName=INDEX_NAME,
        KeyConditionExpression="tipo_nivel_id = :tid",
        ExpressionAttributeValues={":tid": {'S': tipo_id}}
    )
    
    items = [deserialize_item(item) for item in response.get('Items', [])]
    return {"statusCode": 200, "body": json.dumps(items)}