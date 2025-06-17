# services/asistencia-service/resumen_por_nivel.py
import os, json, boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")
    
TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['NIVEL_INDEX']

def handler(event, context):
    nivel_id = event['pathParameters']['nivel_id']
    response = dynamodb_client.query(
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