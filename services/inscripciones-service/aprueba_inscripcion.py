import os
import json
import uuid
import boto3
import random
import string
from werkzeug.security import generate_password_hash

DYNAMODB = boto3.client("dynamodb")
SES = boto3.client("ses", region_name=os.environ.get("AWS_REGION", "us-east-1"))

INS_TABLE = os.environ["DYNAMODB_TABLE"]
USER_TABLE = os.environ["USER_TABLE"]
STUDENT_ROLE_ID = os.environ["STUDENT_ROLE_ID"]
SES_SOURCE_EMAIL = os.environ["SES_SOURCE_EMAIL"]

def generate_temp_password(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def handler(event, context):
    cors_headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }
    insc_id = event.get("pathParameters", {}).get("id")
    try:
        resp = DYNAMODB.get_item(
            TableName=INS_TABLE,
            Key={"id": {"S": insc_id}}
        )
        item = resp.get("Item")
        if not item:
            return {
                "statusCode": 404,
                "headers": cors_headers,
                "body": json.dumps({"success": False, "message": "Inscripción no encontrada"})
            }
        insc = {k: list(v.values())[0] for k, v in item.items()}
        # activamos
        DYNAMODB.update_item(
            TableName=INS_TABLE,
            Key={"id": {"S": insc_id}},
            UpdateExpression="SET #s=:a",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":a": {"S": "active"}}
        )
        # contraseña
        temp_pass = generate_temp_password()
        hashed = generate_password_hash(temp_pass)
        user_id = str(uuid.uuid4())
        DYNAMODB.put_item(
            TableName=USER_TABLE,
            Item={
                "id": {"S": user_id},
                "nombre": {"S": insc.get("studentName", "")},
                "email": {"S": insc.get("email", "")},
                "password_hash": {"S": hashed},
                "rol": {"S": STUDENT_ROLE_ID},
                "telefono": {"S": insc.get("phone", "")}
            }
        )
        # correo
        SES.send_email(
            Source=SES_SOURCE_EMAIL,
            Destination={"ToAddresses": [insc["email"]]},
            Message={
                "Subject": {"Data": "Inscripción Aprobada - Diamond's Academy"},
                "Body": {
                    "Text": {
                        "Data": (
                            f"Hola {insc['studentName']},\n\n"
                            f"Tu inscripción fue aprobada. Tu contraseña temporal es: {temp_pass}\n"
                            "Por favor cámbiala al ingresar."
                        )
                    }
                }
            }
        )
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({"success": True, "message": "Inscripción aprobada y usuario creado."})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({"success": False, "message": f"Error interno: {e}"})
        }