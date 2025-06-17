import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    response = DYNAMODB_CLIENT.scan(TableName=TABLE_NAME)
    items = [deserialize_item(item) for item in response.get('Items', [])]
    return {"statusCode": 200, "body": json.dumps(items)}