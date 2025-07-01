import os
import json
from utils import get_dynamodb_client, deserialize_item
import boto3

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['TIPO_NIVEL_INDEX']

def handler(event, context):
    tipo_id = event['pathParameters'].get('tipo_id')
    if not tipo_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "El 'tipo_id' es requerido en la ruta."})
        }

    # Revisamos si nos piden solo los niveles con cupos disponibles
    params = event.get('queryStringParameters') or {}
    solo_disponibles = params.get('soloDisponibles', 'false').lower() == 'true'

    # Construimos la llamada al GSI
    query_args = {
        'TableName': TABLE_NAME,
        'IndexName': INDEX_NAME,
        'KeyConditionExpression': "tipo_nivel_id = :tid",
        'ExpressionAttributeValues': {":tid": {'S': tipo_id}}
    }

    # Si piden solo disponibles, agregamos FilterExpression
    if solo_disponibles:
        query_args['FilterExpression'] = "cupos_actuales < cupos_maximos"

    try:
        resp = DYNAMODB_CLIENT.query(**query_args)
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error en consulta a DynamoDB: {str(e)}"})
        }

    items = [deserialize_item(item) for item in resp.get('Items', [])]
    return {
        "statusCode": 200,
        "body": json.dumps(items)
    }
