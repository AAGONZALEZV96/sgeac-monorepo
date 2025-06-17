import os, json, uuid
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    nombre = data.get('nombre')
    tipo_nivel_id = data.get('tipo_nivel_id')
    maestra_id = data.get('maestra_id')

    if not all([nombre, tipo_nivel_id, maestra_id]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos."})}

    item = {
        'id': {'S': str(uuid.uuid4())},
        'nombre': {'S': nombre},
        'rango_edad': {'S': data.get('rango_edad', 'N/A')},
        'horario': {'S': data.get('horario', 'N/A')},
        'tipo_nivel_id': {'S': tipo_nivel_id},
        'maestra_id': {'S': maestra_id},
        'cupos_maximos': {'N': '10'},
        'cupos_actuales': {'N': '0'}
    }

    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    
    # Preparamos una respuesta limpia
    response_body = {
        "id": item['id']['S'],
        "nombre": item['nombre']['S'],
        "rango_edad": item['rango_edad']['S'],
        "horario": item['horario']['S'],
        "tipo_nivel_id": item['tipo_nivel_id']['S'],
        "maestra_id": item['maestra_id']['S'],
        "cupos_maximos": int(item['cupos_maximos']['N']),
        "cupos_actuales": int(item['cupos_actuales']['N'])
    }
    return {"statusCode": 201, "body": json.dumps(response_body)}