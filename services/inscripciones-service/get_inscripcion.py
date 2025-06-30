import os
import json
import boto3

DYNAMODB = boto3.client("dynamodb")
TABLE_NAME = os.environ["DYNAMODB_TABLE"]

def handler(event, context):
    cors_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
    insc_id = event.get("pathParameters", {}).get("id")
    try:
        resp = DYNAMODB.get_item(
            TableName=TABLE_NAME,
            Key={"id": {"S": insc_id}}
        )
        item = resp.get("Item")
        if not item:
            return {
                "statusCode": 404,
                "headers": cors_headers,
                "body": json.dumps({"message": "Inscripción no encontrada"})
            }
        result = {k: list(v.values())[0] for k, v in item.items()}
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps(result)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({"message": f"Error interno: {e}"})
        }