import os
import json
import uuid
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    # Atributos del nivel, incluyendo los IDs de las relaciones
    nombre = data.get('nombre')
    rango_edad = data.get('rango_edad')
    horario = data.get('horario')
    tipo_nivel_id = data.get('tipo_nivel_id') # ID del Tipo de Nivel
    maestra_id = data.get('maestra_id')       # ID de la Maestra (Usuario)

    if not all([nombre, tipo_nivel_id, maestra_id]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos: nombre, tipo_nivel_id, maestra_id."})}

    item = {
        'id': {'S': str(uuid.uuid4())},
        'nombre': {'S': nombre},
        'rango_edad': {'S': rango_edad},
        'horario': {'S': horario},
        'tipo_nivel_id': {'S': tipo_nivel_id},
        'maestra_id': {'S': maestra_id},
        'cupos_maximos': {'N': '10'},  # ¡NUEVO! Se establece la capacidad máxima
        'cupos_actuales': {'N': '0'}   # ¡NUEVO! Se inicializa en 0
    }

    dynamodb_client.put_item(TableName=TABLE_NAME, Item=item)
    
    # Preparamos una respuesta limpia para el cliente
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