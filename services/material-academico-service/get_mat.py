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
    """Convierte un item de DynamoDB a un diccionario de Python."""
    return {key: list(val.values())[0] for key, val in item.items()}

def handler(event, context):
    try:
        material_id = event['pathParameters']['id']
        response = dynamodb_client.get_item(
            TableName=TABLE_NAME, 
            Key={'id': {'S': material_id}}
        )
        
        if 'Item' in response:
            item = deserialize_item(response['Item'])
            return {"statusCode": 200, "body": json.dumps(item)}
        else:
            return {"statusCode": 44, "body": json.dumps({"error": "Material no encontrado."})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": f"Error interno: {str(e)}"}) }