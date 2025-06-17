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
        # Obtenemos el tipo ('S', 'N', etc.) y el valor
        val_type = list(val_dict.keys())[0]
        value = val_dict[val_type]
        # Si es un número, lo convertimos a entero/flotante
        if val_type == 'N':
            try:
                deserialized[key] = int(value)
            except ValueError:
                deserialized[key] = float(value)
        else:
            deserialized[key] = value
    return deserialized

def handler(event, context):
    """
    Actualiza los datos de un material académico existente.
    """
    try:
        material_id = event['pathParameters']['id']
        data = json.loads(event.get("body", "{}"))

        if not data:
            return {"statusCode": 400, "body": json.dumps({"error": "El cuerpo de la petición no puede estar vacío."})}

        # Construcción dinámica de la expresión de actualización
        update_expression_parts = []
        expression_attribute_values = {}
        
        for key, value in data.items():
            update_expression_parts.append(f"{key} = :{key}")
            # Para esta entidad, todos los atributos son strings
            expression_attribute_values[f":{key}"] = {'S': str(value)}
        
        update_expression = "SET " + ", ".join(update_expression_parts)

        response = dynamodb_client.update_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': material_id}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="ALL_NEW"
        )
        
        updated_item = deserialize_item(response['Attributes'])
        return {"statusCode": 200, "body": json.dumps(updated_item)}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": f"Error interno del servidor: {str(e)}"}) }