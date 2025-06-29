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
        DYNAMODB.update_item(
            TableName=TABLE_NAME,
            Key={"id": {"S": insc_id}},
            UpdateExpression="SET #s = :r",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":r": {"S": "rejected"}}
        )
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({
                "success": True,
                "message": "Inscripción rechazada"
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({
                "success": False,
                "message": f"Error interno: {e}"
            })
        }