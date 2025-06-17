import os, json, uuid
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    nivel_id = data.get('nivel_id')
    nombre = data.get('nombre')
    tipo_archivo = data.get('tipo_archivo')
    enlace_descarga = data.get('enlace_descarga')

    if not all([nivel_id, nombre, tipo_archivo, enlace_descarga]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos."})}

    item = {
        'id': {'S': str(uuid.uuid4())},
        'nivel_id': {'S': nivel_id},
        'nombre': {'S': nombre},
        'tipo_archivo': {'S': tipo_archivo},
        'enlace_descarga': {'S': enlace_descarga}
    }
    
    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    
    response_body = {key: val['S'] for key, val in item.items()}
    return {"statusCode": 201, "body": json.dumps(response_body)}