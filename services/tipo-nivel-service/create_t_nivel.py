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
    tipo_nivel_id = str(uuid.uuid4())
    nombre = data.get('nombre')
    # Obtenemos los nuevos atributos
    edad_minima = data.get('edad_minima')
    edad_maxima = data.get('edad_maxima')

    if not all([nombre, edad_minima is not None, edad_maxima is not None]):
        return {"statusCode": 400, "body": json.dumps({"error": "Los atributos 'nombre', 'edad_minima' y 'edad_maxima' son requeridos."})}

    item = {
        'id': {'S': tipo_nivel_id},
        'nombre': {'S': nombre},
        # Guardamos las edades como números (formato de string para DynamoDB)
        'edad_minima': {'N': str(edad_minima)},
        'edad_maxima': {'N': str(edad_maxima)}
    }

    dynamodb_client.put_item(TableName=TABLE_NAME, Item=item)
    
    response_body = {
        "id": tipo_nivel_id, 
        "nombre": nombre,
        "edad_minima": edad_minima,
        "edad_maxima": edad_maxima
    }
    return {"statusCode": 201, "body": json.dumps(response_body)}