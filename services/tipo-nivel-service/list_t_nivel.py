import os
import json
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def deserialize_item(item):
    return {key: list(val.values())[0] for key, val in item.items()}

def handler(event, context):
    # Parámetros de la consulta en la URL, ej: /users?edad_min=6
    params = event.get('queryStringParameters') or {}
    
    # Preparamos los argumentos para la operación scan
    scan_args = {
        'TableName': TABLE_NAME
    }
    
    # Si hay parámetros de edad, construimos un FilterExpression
    if 'edad_min' in params and 'edad_max' in params:
        scan_args['FilterExpression'] = "edad BETWEEN :min AND :max"
        scan_args['ExpressionAttributeValues'] = {
            ":min": {"N": str(params['edad_min'])},
            ":max": {"N": str(params['edad_max'])}
        }

    # Usamos la operación 'scan' con los argumentos preparados
    response = dynamodb_client.scan(**scan_args)
    
    items = [deserialize_item(item) for item in response.get('Items', [])]
    return {"statusCode": 200, "body": json.dumps(items)}