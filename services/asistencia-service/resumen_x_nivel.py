import os, json
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['NIVEL_INDEX']

def handler(event, context):
    nivel_id = event['pathParameters']['nivel_id']

    response = DYNAMODB_CLIENT.query(
        TableName=TABLE_NAME,
        IndexName=INDEX_NAME,
        KeyConditionExpression="nivel_id = :nid",
        ExpressionAttributeValues={":nid": {'S': nivel_id}}
    )
    items = response.get('Items', [])
    
    presentes = sum(1 for item in items if item.get('estado', {}).get('S') == 'presente')
    ausentes = sum(1 for item in items if item.get('estado', {}).get('S') == 'ausente')
    
    resumen = {"presentes_hoy": presentes, "ausentes_hoy": ausentes, "total_alumnos_registrados_hoy": len(items)}
    return {"statusCode": 200, "body": json.dumps(resumen)}