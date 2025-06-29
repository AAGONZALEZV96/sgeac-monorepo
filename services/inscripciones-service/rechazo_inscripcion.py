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
        dynamodb.update_item(
            TableName=TABLE_NAME,
            Key={"id": {"S": insc_id}},
            UpdateExpression="SET #s = :r",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":r": {"S": "rejected"}}
        )
        return {"statusCode": 200, "headers": cors, "body": json.dumps({"success": True, "message": "Inscripción rechazada"})}
    except Exception as e:
        return {"statusCode": 500, "headers": cors, "body": json.dumps({"success": False, "message": f"Error interno: {str(e)}"})}