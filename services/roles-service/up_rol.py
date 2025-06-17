import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    rol_id = event['pathParameters']['id']
    data = json.loads(event.get("body", "{}"))
    nombre = data.get('nombre')
    if not nombre:
        return {"statusCode": 400, "body": json.dumps({"error": "El atributo 'nombre' es requerido."})}

    response = DYNAMODB_CLIENT.update_item(
        TableName=TABLE_NAME,
        Key={'id': {'S': rol_id}},
        UpdateExpression="SET nombre = :nombre",
        ExpressionAttributeValues={":nombre": {'S': nombre}},
        ReturnValues="ALL_NEW"
    )
    
    updated_item = deserialize_item(response['Attributes'])
    return {"statusCode": 200, "body": json.dumps(updated_item)}