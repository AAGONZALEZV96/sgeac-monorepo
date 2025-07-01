# services/niveles-service/create_nivel.py

import os, json, uuid
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    # Campos obligatorios
    nombre = data.get('nombre')
    tipo_nivel_id = data.get('tipo_nivel_id')
    instructor_id = data.get('instructor_id')
    cupos_maximos = data.get('cupos_maximos')

    # Validación básica
    if not all([nombre, tipo_nivel_id, instructor_id]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos: nombre, tipo_nivel_id, instructor_id."})}

    # cupos_maximos debe ser int > 0
    if not isinstance(cupos_maximos, int) or cupos_maximos <= 0:
        return {"statusCode": 400, "body": json.dumps({"error": "El campo 'cupos_maximos' debe ser un entero positivo."})}

    # Resto de campos
    rango_edad = data.get('rango_edad', 'N/A')
    horario    = data.get('horario', 'N/A')

    item = {
        'id':             {'S': str(uuid.uuid4())},
        'nombre':         {'S': nombre},
        'rango_edad':     {'S': rango_edad},
        'horario':        {'S': horario},
        'tipo_nivel_id':  {'S': tipo_nivel_id},
        'instructor_id':  {'S': instructor_id},
        'cupos_maximos':  {'N': str(cupos_maximos)},
        'cupos_actuales': {'N': '0'}
    }

    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    
    # Respuesta limpia
    response_body = {
        "id":             item['id']['S'],
        "nombre":         item['nombre']['S'],
        "rango_edad":     item['rango_edad']['S'],
        "horario":        item['horario']['S'],
        "tipo_nivel_id":  item['tipo_nivel_id']['S'],
        "instructor_id":  item['instructor_id']['S'],
        "cupos_maximos":  int(item['cupos_maximos']['N']),
        "cupos_actuales": int(item['cupos_actuales']['N'])
    }

    return {"statusCode": 201, "body": json.dumps(response_body)}
