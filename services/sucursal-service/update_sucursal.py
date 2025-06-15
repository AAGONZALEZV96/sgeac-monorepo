import os
import json
import boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    sucursal_id = event['pathParameters']['id']
    body = json.loads(event.get("body", "{}"))
    
    update_expression_parts = []
    expression_attribute_values = {}
    
    for key, value in body.items():
        update_expression_parts.append(f"{key} = :{key}")
        expression_attribute_values[f":{key}"] = {'S': str(value)} # Asumimos todos strings
        
    update_expression = "SET " + ", ".join(update_expression_parts)

    response = dynamodb_client.update_item(
        TableName=TABLE_NAME,
        Key={'id': {'S': sucursal_id}},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="ALL_NEW"
    )
    
    # El deserializer de get.py no sirve aquí porque la respuesta de update_item tiene otro formato
    updated_attributes = {key: list(val.values())[0] for key, val in response.get('Attributes').items()}

    return { "statusCode": 200, "body": json.dumps(updated_attributes) }