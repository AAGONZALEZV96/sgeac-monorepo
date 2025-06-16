import os
import json
import uuid
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    rol_id = str(uuid.uuid4())
    nombre = data.get('nombre')

    if not nombre:
        return {"statusCode": 400, "body": json.dumps({"error": "El atributo 'nombre' es requerido."})}

    item = {
        'id': {'S': rol_id},
        'nombre': {'S': nombre}
    }

    dynamodb_client.put_item(TableName=TABLE_NAME, Item=item)
    
    response_body = {"id": rol_id, "nombre": nombre}
    return {"statusCode": 201, "body": json.dumps(response_body)}