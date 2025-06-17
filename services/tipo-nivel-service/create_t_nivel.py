import os, json, uuid
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    nombre = data.get('nombre')
    edad_minima = data.get('edad_minima')
    edad_maxima = data.get('edad_maxima')

    if not all([nombre, edad_minima is not None, edad_maxima is not None]):
        return {"statusCode": 400, "body": json.dumps({"error": "Los atributos 'nombre', 'edad_minima' y 'edad_maxima' son requeridos."})}

    tipo_nivel_id = str(uuid.uuid4())
    item = {
        'id': {'S': tipo_nivel_id},
        'nombre': {'S': nombre},
        'edad_minima': {'N': str(edad_minima)},
        'edad_maxima': {'N': str(edad_maxima)}
    }
    
    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    
    response_body = {
        "id": tipo_nivel_id,
        "nombre": nombre,
        "edad_minima": edad_minima,
        "edad_maxima": edad_maxima
    }
    return {"statusCode": 201, "body": json.dumps(response_body)}