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
    status = event.get("queryStringParameters", {}).get("status") if event.get("queryStringParameters") else None
    try:
        if status:
            resp = DYNAMODB.query(
                TableName=TABLE_NAME,
                IndexName="status-index",
                KeyConditionExpression="status = :s",
                ExpressionAttributeValues={":s": {"S": status}}
            )
            items = resp.get("Items", [])
        else:
            resp = DYNAMODB.scan(TableName=TABLE_NAME)
            items = resp.get("Items", [])
        result = [{k: list(v.values())[0] for k, v in i.items()} for i in items]
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