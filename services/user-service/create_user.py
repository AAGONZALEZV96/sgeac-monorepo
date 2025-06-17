import os, json, uuid
from utils import get_dynamodb_client
from werkzeug.security import generate_password_hash

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    password = data.get('password')

    if not password:
        return {"statusCode": 400, "body": json.dumps({"error": "La contraseña es requerida."})}

    password_hash = generate_password_hash(password)

    item = {
        'id': {'S': str(uuid.uuid4())},
        'email': {'S': data.get('email')},
        'password_hash': {'S': password_hash}, # Guardamos el hash
        'nombre': {'S': data.get('nombre')},
        'rol': {'S': data.get('rol')},
        'rut': {'S': data.get('rut')},
        'edad': {'N': str(data.get('edad'))},
        'telefono': {'S': data.get('telefono')},
        'direccion': {'S': data.get('direccion')},
        'sucursal': {'S': data.get('sucursal')}
    }
    
    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    return {"statusCode": 201, "body": json.dumps({"message": "Usuario creado."})}