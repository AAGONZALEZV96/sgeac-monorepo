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
    try:
        calificacion_id = event['pathParameters']['id']
        data = json.loads(event.get("body", "{}"))

        if not data:
            return {"statusCode": 400, "body": json.dumps({"error": "El cuerpo de la petición no puede estar vacío."})}

        update_expression_parts = []
        expression_attribute_values = {}
        
        for key, value in data.items():
            update_expression_parts.append(f"{key} = :{key}")
            if key == 'nota':
                expression_attribute_values[f":{key}"] = {'N': str(value)}
            else:
                expression_attribute_values[f":{key}"] = {'S': str(value)}
        
        update_expression = "SET " + ", ".join(update_expression_parts)

        dynamodb_client.update_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': calificacion_id}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        return {"statusCode": 200, "body": json.dumps({"message": "Calificación actualizada exitosamente."})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": f"Error interno: {str(e)}"}) }