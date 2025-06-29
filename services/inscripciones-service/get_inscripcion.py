import os
import json
import boto3
from utils import get_dynamodb_client

dynamodb = get_dynamodb_client()
TABLE_NAME = os.environ.get("DYNAMODB_TABLE")


def handler(event, context):
    cors = {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}
    insc_id = event.get("pathParameters", {}).get("id")
    try:
        resp = dynamodb.get_item(
            TableName=TABLE_NAME,
            Key={"id": {"S": insc_id}}
        )
        item = resp.get("Item")
        if not item:
            return {"statusCode": 404, "headers": cors, "body": json.dumps({"message": "Inscripción no encontrada"})}
        result = {k: list(v.values())[0] for k, v in item.items()}
        return {"statusCode": 200, "headers": cors, "body": json.dumps(result)}
    except Exception as e:
        return {"statusCode": 500, "headers": cors, "body": json.dumps({"message": f"Error interno: {str(e)}"})}