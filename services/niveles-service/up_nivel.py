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
    Actualiza los datos de un nivel existente.
    """
    try:
        nivel_id = event['pathParameters']['id']
        data = json.loads(event.get("body", "{}"))

        if not data:
            return {"statusCode": 400, "body": json.dumps({"error": "El cuerpo de la petición no puede estar vacío."})}

        update_expression_parts = []
        expression_attribute_values = {}
        
        for key, value in data.items():
            update_expression_parts.append(f"{key} = :{key}")
            # Determina el tipo de dato para DynamoDB
            if key in ['cupos_maximos', 'cupos_actuales']:
                expression_attribute_values[f":{key}"] = {'N': str(value)}
            else: # El resto se trata como string
                expression_attribute_values[f":{key}"] = {'S': str(value)}
        
        update_expression = "SET " + ", ".join(update_expression_parts)

        response = dynamodb_client.update_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': nivel_id}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="ALL_NEW"
        )
        
        updated_item = deserialize_item(response['Attributes'])
        return {"statusCode": 200, "body": json.dumps(updated_item)}

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno del servidor: {str(e)}"})
        }