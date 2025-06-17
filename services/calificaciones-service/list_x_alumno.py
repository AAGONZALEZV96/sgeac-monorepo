import os
import json
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['ALUMNO_INDEX']

def deserialize_item(item):
    """
    VERSIÓN CORREGIDA: Convierte un item de DynamoDB a un diccionario de Python.
    Maneja correctamente tanto números enteros como decimales (flotantes).
    """
    deserialized = {}
    for key, val_dict in item.items():
        val_type = list(val_dict.keys())[0]
        value = val_dict[val_type]
        
        # Si el tipo es Número ('N')...
        if val_type == 'N':
            # ...intenta convertirlo a entero.
            try:
                deserialized[key] = int(value)
            # Si falla (porque es un decimal como "6.5"), conviértelo a flotante.
            except ValueError:
                deserialized[key] = float(value)
        else:
            # Si no es un número, trátalo como texto.
            deserialized[key] = value
    return deserialized

def handler(event, context):
    """
    Handler para buscar y devolver todas las calificaciones de un alumno usando un GSI.
    """
    try:
        alumno_id = event['pathParameters']['alumno_id']

        response = dynamodb_client.query(
            TableName=TABLE_NAME,
            IndexName=INDEX_NAME,
            KeyConditionExpression="alumno_id = :aid",
            ExpressionAttributeValues={":aid": {'S': alumno_id}}
        )
        
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