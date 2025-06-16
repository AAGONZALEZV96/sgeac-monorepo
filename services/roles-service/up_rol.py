import os
import json
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def deserialize_item(item):
    return {key: list(val.values())[0] for key, val in item.items()}

def handler(event, context):
    rol_id = event['pathParameters']['id']
    data = json.loads(event.get("body", "{}"))
    nombre = data.get('nombre')

    if not nombre:
        return {"statusCode": 400, "body": json.dumps({"error": "El atributo 'nombre' es requerido."})}

    response = dynamodb_client.update_item(
        TableName=TABLE_NAME,
        Key={'id': {'S': rol_id}},
        UpdateExpression="SET nombre = :nombre",
        ExpressionAttributeValues={":nombre": {'S': nombre}},
        ReturnValues="ALL_NEW"
    )
    
    updated_attributes = deserialize_item(response['Attributes'])
    return {"statusCode": 200, "body": json.dumps(updated_attributes)}