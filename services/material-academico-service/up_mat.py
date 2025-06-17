import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    material_id = event['pathParameters']['id']
    data = json.loads(event.get("body", "{}"))

    if not data:
        return {"statusCode": 400, "body": json.dumps({"error": "El cuerpo de la petición no puede estar vacío."})}

    update_expression_parts = []
    expression_attribute_values = {}
    
    for key, value in data.items():
        update_expression_parts.append(f"{key} = :{key}")
        expression_attribute_values[f":{key}"] = {'S': str(value)}
    
    update_expression = "SET " + ", ".join(update_expression_parts)

    response = DYNAMODB_CLIENT.update_item(
        TableName=TABLE_NAME, Key={'id': {'S': material_id}},
        UpdateExpression=update_expression, ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="ALL_NEW"
    )
    
    updated_item = deserialize_item(response['Attributes'])
    return {"statusCode": 200, "body": json.dumps(updated_item)}