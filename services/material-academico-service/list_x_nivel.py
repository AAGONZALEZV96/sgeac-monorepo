import os, json, boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['NIVEL_INDEX']

def deserialize_item(item):
    return {key: list(val.values())[0] for key, val in item.items()}

def handler(event, context):
    nivel_id = event['pathParameters']['nivel_id']

    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        IndexName=INDEX_NAME,
        KeyConditionExpression="nivel_id = :nid",
        ExpressionAttributeValues={":nid": {'S': nivel_id}}
    )
    
    items = [deserialize_item(item) for item in response.get('Items', [])]
    return {"statusCode": 200, "body": json.dumps(items)}