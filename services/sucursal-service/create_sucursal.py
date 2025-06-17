import os, json, uuid
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    # Atributos de la sucursal 
    nombre = data.get('nombre')
    direccion = data.get('direccion')
    telefono = data.get('telefono')
    correo_contacto = data.get('correo_contacto')
    comuna = data.get('comuna')

    if not nombre or not direccion:
        return {"statusCode": 400, "body": json.dumps({"error": "Los atributos 'nombre' y 'direccion' son requeridos."})}
    
    sucursal_id = str(uuid.uuid4())
    item = {
        'id': {'S': sucursal_id},
        'nombre': {'S': nombre},
        'direccion': {'S': direccion},
        'telefono': {'S': telefono or 'N/A'},
        'correo_contacto': {'S': correo_contacto or 'N/A'},
        'comuna': {'S': comuna or 'N/A'}
    }
    
    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    
    response_body = {key: val['S'] for key, val in item.items()}
    return {"statusCode": 201, "body": json.dumps(response_body)}