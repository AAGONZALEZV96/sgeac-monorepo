import os
import json
import uuid
import boto3
import random
import string
from werkzeug.security import generate_password_hash
from utils import get_dynamodb_client

# Cliente DynamoDB (LocalStack o AWS real)
dynamodb = get_dynamodb_client()

INS_TABLE       = os.environ["DYNAMODB_TABLE"]
USER_TABLE      = os.environ["USER_TABLE"]
STUDENT_ROLE_ID = os.environ["STUDENT_ROLE_ID"]

def generate_temp_password(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def handler(event, context):
    cors = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }
    insc_id = event.get("pathParameters", {}).get("id")

    try:
        # 1) Leer la inscripción
        resp = dynamodb.get_item(
            TableName=INS_TABLE,
            Key={"id": {"S": insc_id}}
        )
        item = resp.get("Item")
        if not item:
            return {
                "statusCode": 404,
                "headers": cors,
                "body": json.dumps({"success": False, "message": "Inscripción no encontrada"})
            }
        insc = {k: list(v.values())[0] for k, v in item.items()}

        # 2) Marcar como 'active'
        dynamodb.update_item(
            TableName=INS_TABLE,
            Key={"id": {"S": insc_id}},
            UpdateExpression="SET #s = :a",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":a": {"S": "active"}}
        )

        # 3) Crear usuario con contraseña temporal
        temp_pass = generate_temp_password()
        hashed    = generate_password_hash(temp_pass)
        user_id   = str(uuid.uuid4())
        dynamodb.put_item(
            TableName=USER_TABLE,
            Item={
                "id":            {"S": user_id},
                "nombre":        {"S": insc.get("studentName", "")},
                "email":         {"S": insc.get("email", "")},
                "password_hash": {"S": hashed},
                "rol":           {"S": STUDENT_ROLE_ID},
                "telefono":      {"S": insc.get("phone", "")}
            }
        )

        # Ya no enviamos ningún correo

        return {
            "statusCode": 200,
            "headers": cors,
            "body": json.dumps({
                "success": True,
                "message": "Inscripción aprobada y usuario creado."
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors,
            "body": json.dumps({
                "success": False,
                "message": f"Error interno: {str(e)}"
            })
        }