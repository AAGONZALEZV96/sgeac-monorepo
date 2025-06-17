import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    rol_id = event['pathParameters']['id']
    response = DYNAMODB_CLIENT.get_item(TableName=TABLE_NAME, Key={'id': {'S': rol_id}})
    item = deserialize_item(response.get('Item'))
    
    if item:
        return {"statusCode": 200, "body": json.dumps(item)}
    else:
        return {"statusCode": 404, "body": json.dumps({"error": "Rol no encontrado."})}