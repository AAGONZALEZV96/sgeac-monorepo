import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    user_id = event['pathParameters']['id']
    response = DYNAMODB_CLIENT.get_item(TableName=TABLE_NAME, Key={'id': {'S': user_id}})
    item = deserialize_item(response.get('Item'))
    
    if item:
        # Por seguridad, nunca devolvemos el hash de la contraseña
        item.pop('password_hash', None)
        return {"statusCode": 200, "body": json.dumps(item)}
    else:
        return {"statusCode": 404, "body": json.dumps({"error": "Usuario no encontrado."})}