import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['ALUMNO_INDEX']

def handler(event, context):
    alumno_id = event['pathParameters']['alumno_id']
    response = DYNAMODB_CLIENT.query(
        TableName=TABLE_NAME,
        IndexName=INDEX_NAME,
        KeyConditionExpression="alumno_id = :aid",
        ExpressionAttributeValues={":aid": {'S': alumno_id}}
    )
    # La única diferencia con la función de resumen es que aquí devolvemos los items completos.
    items = [deserialize_item(item) for item in response.get('Items', [])]
    return {"statusCode": 200, "body": json.dumps(items)}