import os, json
from utils import get_dynamodb_client

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
    items = response.get('Items', [])
    
    presentes = sum(1 for item in items if item.get('estado', {}).get('S') == 'presente')
    ausentes = sum(1 for item in items if item.get('estado', {}).get('S') == 'ausente')
    
    resumen = {"presentes": presentes, "ausentes": ausentes, "total": len(items)}
    return {"statusCode": 200, "body": json.dumps(resumen)}