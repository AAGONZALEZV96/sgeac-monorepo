import os, json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    params = event.get('queryStringParameters') or {}
    scan_args = {'TableName': TABLE_NAME}
    filter_expressions = []
    expression_attribute_values = {}

    if 'edad_min' in params and 'edad_max' in params:
        filter_expressions.append("edad BETWEEN :min AND :max")
        expression_attribute_values[":min"] = {"N": str(params['edad_min'])}
        expression_attribute_values[":max"] = {"N": str(params['edad_max'])}

    if 'rol' in params:
        filter_expressions.append("rol = :rol")
        expression_attribute_values[":rol"] = {"S": params['rol']}

    if filter_expressions:
        scan_args['FilterExpression'] = " AND ".join(filter_expressions)
        scan_args['ExpressionAttributeValues'] = expression_attribute_values

    response = DYNAMODB_CLIENT.scan(**scan_args)
    items = [deserialize_item(item) for item in response.get('Items', [])]
    return {"statusCode": 200, "body": json.dumps(items)}