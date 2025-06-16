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
    Convierte un item de formato DynamoDB a un diccionario de Python.
    """
    deserialized = {}
    for key, val_dict in item.items():
        val_type = list(val_dict.keys())[0]
        value = val_dict[val_type]
        if val_type == 'N':
            deserialized[key] = int(value)
        else:
            deserialized[key] = value
    return deserialized

def handler(event, context):
    """
    Handler para obtener un nivel por su ID.
    """
    try:
        nivel_id = event['pathParameters']['id']
        response = dynamodb_client.get_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': nivel_id}}
        )
        
        if 'Item' in response:
            item = deserialize_item(response['Item'])
            return {"statusCode": 200, "body": json.dumps(item)}
        else:
            return {"statusCode": 404, "body": json.dumps({"error": "Nivel no encontrado."})}
            
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno del servidor: {str(e)}"})
        }