import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    user_id = event['pathParameters']['id']
    data = json.loads(event.get("body", "{}"))

    if not data:
        return {"statusCode": 400, "body": json.dumps({"error": "El cuerpo de la petición no puede estar vacío."})}

    update_expression_parts = []
    expression_attribute_values = {}
    
    for key, value in data.items():
        if key == 'password': # Si se actualiza la contraseña, la hasheamos
             from werkzeug.security import generate_password_hash
             value = generate_password_hash(value)
             key = 'password_hash' # Actualizamos el campo del hash

        update_expression_parts.append(f"{key} = :{key}")
        if key == 'edad':
            expression_attribute_values[f":{key}"] = {'N': str(value)}
        else:
            expression_attribute_values[f":{key}"] = {'S': str(value)}
    
    update_expression = "SET " + ", ".join(update_expression_parts)

    response = DYNAMODB_CLIENT.update_item(
        TableName=TABLE_NAME,
        Key={'id': {'S': user_id}},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="ALL_NEW"
    )
    
    updated_item = deserialize_item(response['Attributes'])
    updated_item.pop('password_hash', None)
    return {"statusCode": 200, "body": json.dumps(updated_item)}