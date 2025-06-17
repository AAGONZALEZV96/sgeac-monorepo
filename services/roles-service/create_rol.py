import os, json, uuid
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    nombre = data.get('nombre')
    if not nombre:
        return {"statusCode": 400, "body": json.dumps({"error": "El atributo 'nombre' es requerido."})}
    
    rol_id = str(uuid.uuid4())
    item = {'id': {'S': rol_id}, 'nombre': {'S': nombre}}
    
    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    
    return {"statusCode": 201, "body": json.dumps({"id": rol_id, "nombre": nombre})}