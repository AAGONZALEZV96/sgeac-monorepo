import os
import json
import uuid
from datetime import datetime
import boto3

# Cliente de DynamoDB
DYNAMODB = boto3.client("dynamodb")
TABLE_NAME = os.environ["DYNAMODB_TABLE"]

def handler(event, context):
    cors_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }
    try:
        body = event.get("body", "{}")
        data = json.loads(body)
        required = [
            "studentName", "studentAge", "email", "phone",
            "classType", "experience", "schedule"
        ]
        for f in required:
            if not data.get(f):
                return {
                    "statusCode": 400,
                    "headers": cors_headers,
                    "body": json.dumps({
                        "success": False,
                        "message": f"Falta el campo {f}"
                    })
                }
        item = {
            "id": {"S": str(uuid.uuid4())},
            **{k: {"S": data.get(k, "")} for k in [
                "studentName", "studentAge", "parentName", "email", "phone",
                "classType", "experience", "schedule", "medicalInfo", "comments"
            ]},
            "status": {"S": "pending"},
            "submittedAt": {"S": datetime.utcnow().isoformat()}
        }
        DYNAMODB.put_item(TableName=TABLE_NAME, Item=item)
        return {
            "statusCode": 201,
            "headers": cors_headers,
            "body": json.dumps({
                "success": True,
                "message": "Inscripción creada exitosamente"
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
