import os
import json
import boto3
from utils import get_dynamodb_client

dynamodb = get_dynamodb_client()
TABLE_NAME = os.environ["DYNAMODB_TABLE"]

def handler(event, context):
    cors_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }

    # Leemos el parámetro status (pending, active, etc.)
    params = event.get("queryStringParameters") or {}
    status = params.get("status")

    try:
        if status:
            # Escapamos el nombre del atributo con ExpressionAttributeNames
            resp = dynamodb.scan(
                TableName=TABLE_NAME,
                FilterExpression="#st = :s",
                ExpressionAttributeNames={"#st": "status"},
                ExpressionAttributeValues={":s": {"S": status}}
            )
        else:
            resp = dynamodb.scan(TableName=TABLE_NAME)

        items = resp.get("Items", [])
        # Deserializamos cada item:
        result = [
            {k: list(v.values())[0] for k, v in item.items()}
            for item in items
        ]

        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({"message": f"Error interno: {str(e)}"})
        }