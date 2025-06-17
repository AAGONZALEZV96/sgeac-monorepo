import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['NIVEL_INDEX']

def handler(event, context):
    nivel_id = event['pathParameters']['nivel_id']

    response = DYNAMODB_CLIENT.query(
        TableName=TABLE_NAME, IndexName=INDEX_NAME,
        KeyConditionExpression="nivel_id = :nid",
        ExpressionAttributeValues={":nid": {'S': nivel_id}}
    )
    
    items = [deserialize_item(item) for item in response.get('Items', [])]
    return {"statusCode": 200, "body": json.dumps(items)}