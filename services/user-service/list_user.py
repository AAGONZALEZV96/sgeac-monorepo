# services/user-service/list.py

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
    """
    NUEVA VERSIÓN: Convierte un item de DynamoDB a un diccionario de Python de forma dinámica.
    No importa qué atributos tenga el item, los procesará todos.
    """
    deserialized = {}
    for key, val_dict in item.items():
        # Obtenemos el tipo de dato ('S', 'N', etc.) y el valor
        val_type = list(val_dict.keys())[0]
        value = val_dict[val_type]
        
        # Si es un número ('N'), lo convertimos a entero
        if val_type == 'N':
            deserialized[key] = int(value)
        else:
            deserialized[key] = value
    return deserialized

def handler(event, context):
    """
    Handler para escanear y devolver todos los usuarios, ahora de forma flexible.
    """
    try:
        # Los parámetros de la URL para el filtro de edad se mantienen igual
        params = event.get('queryStringParameters') or {}
        
        scan_args = {'TableName': TABLE_NAME}
        
        if 'edad_min' in params and 'edad_max' in params:
            scan_args['FilterExpression'] = "edad BETWEEN :min AND :max"
            scan_args['ExpressionAttributeValues'] = {
                ":min": {"N": str(params['edad_min'])},
                ":max": {"N": str(params['edad_max'])}
            }

        response = dynamodb_client.scan(**scan_args)
        
        # Usamos la nueva función para deserializar cada item encontrado
        items = [deserialize_item(item) for item in response.get('Items', [])]
        
        return {
            "statusCode": 200,
            "body": json.dumps(items)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno del servidor: {str(e)}"})
        }