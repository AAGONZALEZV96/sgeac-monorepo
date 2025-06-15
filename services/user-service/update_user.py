import os
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client(
        "dynamodb", endpoint_url="http://localhost.localstack.cloud:4566"
    )
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    """
    Handler para actualizar los datos de un usuario existente.
    """
    try:
        # Extraer el ID de la URL
        user_id = event['pathParameters']['id']

        # Cargar los datos del cuerpo de la solicitud
        body = json.loads(event.get("body", "{}"))

        # Construir la expresión de actualización de DynamoDB
        # Esto permite actualizar solo los campos que vienen en la petición
        update_expression = "SET "
        expression_attribute_values = {}
        
        # Iteramos sobre los datos recibidos para construir la consulta dinámicamente
        for key, value in body.items():
            # Usamos placeholders como ':nombre' para los valores
            placeholder = f":{key}"
            update_expression += f"{key} = {placeholder}, "
            # El formato del valor depende de su tipo (String, Number, etc.)
            # Para este ejemplo, asumimos strings excepto para 'edad'
            if key == 'edad':
                expression_attribute_values[placeholder] = {'N': str(value)}
            else:
                expression_attribute_values[placeholder] = {'S': str(value)}
        
        # Quitar la última coma y espacio ", "
        update_expression = update_expression.strip(", ")

        # Ejecutar la actualización en DynamoDB
        response = dynamodb_client.update_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': user_id}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="ALL_NEW"  # Devuelve el item completo después de la actualización
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response.get('Attributes'))
        }

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Ocurrió un error interno al actualizar el usuario."})
        }