import os
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def deserialize_item(item):
    """Convierte un item de formato DynamoDB a un diccionario de Python."""
    deserialized = {}
    for key, val_dict in item.items():
        # Obtenemos el tipo ('S', 'N', etc.) y el valor
        val_type = list(val_dict.keys())[0]
        value = val_dict[val_type]
        # Si es un número, lo convertimos a entero
        if val_type == 'N':
            deserialized[key] = int(value)
        else:
            deserialized[key] = value
    return deserialized

def handler(event, context):
    """
    Actualiza los datos de un tipo de nivel existente, incluyendo rangos de edad.
    """
    try:
        tipo_nivel_id = event['pathParameters']['id']
        data = json.loads(event.get("body", "{}"))

        if not data:
            return {"statusCode": 400, "body": json.dumps({"error": "El cuerpo de la petición no puede estar vacío."})}

        # Construcción dinámica de la expresión de actualización
        update_expression_parts = []
        expression_attribute_values = {}
        
        for key, value in data.items():
            # Añade la parte de la expresión, ej: "nombre = :nombre"
            update_expression_parts.append(f"{key} = :{key}")
            
            # Asigna el valor y su tipo para DynamoDB
            if key in ['edad_minima', 'edad_maxima']:
                expression_attribute_values[f":{key}"] = {'N': str(value)}
            else: # Asumimos que el resto son strings
                expression_attribute_values[f":{key}"] = {'S': str(value)}
        
        update_expression = "SET " + ", ".join(update_expression_parts)

        # Ejecutamos la actualización en DynamoDB
        response = dynamodb_client.update_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': tipo_nivel_id}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="ALL_NEW"  # Devuelve todos los atributos del item actualizado
        )
        
        # Deserializamos la respuesta para devolver un JSON limpio
        updated_item = deserialize_item(response['Attributes'])

        return {"statusCode": 200, "body": json.dumps(updated_item)}

    except Exception as e:
        logger.error(f"Error inesperado al actualizar: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": "Error interno del servidor."})}