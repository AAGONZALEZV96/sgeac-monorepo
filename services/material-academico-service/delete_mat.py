import os, json
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    material_id = event['pathParameters']['id']
    DYNAMODB_CLIENT.delete_item(TableName=TABLE_NAME, Key={'id': {'S': material_id}})
    return {"statusCode": 200, "body": json.dumps({"message": "Material eliminado exitosamente."})}