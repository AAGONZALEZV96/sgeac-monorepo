import os
import json
import uuid
from datetime import datetime
import boto3
from utils import get_dynamodb_client

# Cliente configurado (LocalStack o real)
dynamodb = get_dynamodb_client()
TABLE_NAME = os.environ.get("DYNAMODB_TABLE")


def handler(event, context):
    cors = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }
    try:
        data = json.loads(event.get("body", "{}"))
        required = [
            "studentName", "studentAge", "email", "phone",
            "classType", "experience", "schedule"
        ]
        for field in required:
            if not data.get(field):
                return {
                    "statusCode": 400,
                    "headers": cors,
                    "body": json.dumps({
                        "success": False,
                        "message": f"Falta el campo obligatorio: {field}"
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
        dynamodb.put_item(TableName=TABLE_NAME, Item=item)
        return {
            "statusCode": 201,
            "headers": cors,
            "body": json.dumps({"success": True, "message": "Inscripción creada exitosamente"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors,
            "body": json.dumps({"success": False, "message": f"Error interno: {str(e)}"})
        }