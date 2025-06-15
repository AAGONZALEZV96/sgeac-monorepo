import os
import json
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    sucursal_id = event['pathParameters']['id']
    dynamodb_client.delete_item(TableName=TABLE_NAME, Key={'id': {'S': sucursal_id}})
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Sucursal eliminada exitosamente."})
    }