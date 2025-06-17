import os, json, boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['ALUMNO_INDEX']

def handler(event, context):
    alumno_id = event['pathParameters']['alumno_id']
    response = dynamodb_client.query(
        TableName=TABLE_NAME,
        IndexName=INDEX_NAME,
        KeyConditionExpression="alumno_id = :aid",
        ExpressionAttributeValues={":aid": {'S': alumno_id}}
    )
    items = response.get('Items', [])
    
    # Contamos los estados
    presentes = sum(1 for item in items if item.get('estado', {}).get('S') == 'presente')
    ausentes = sum(1 for item in items if item.get('estado', {}).get('S') == 'ausente')
    
    resumen = {"presentes": presentes, "ausentes": ausentes, "total": len(items)}
    return {"statusCode": 200, "body": json.dumps(resumen)}