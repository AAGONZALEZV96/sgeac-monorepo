import os
import json
import boto3
from werkzeug.security import generate_password_hash
from utils import get_dynamodb_client

dynamodb = get_dynamodb_client()
INSCRIPCIONES_TABLE = os.environ["DYNAMODB_TABLE"]   # tabla de inscripciones
USUARIOS_TABLE      = os.environ["USER_TABLE"]       # tabla de usuarios

def handler(event, context):
    insc_id = event["pathParameters"]["id"]

    # 1) Actualizar status de la inscripción a "active"
    try:
        dynamodb.update_item(
            TableName=INSCRIPCIONES_TABLE,
            Key={"id": {"S": insc_id}},
            UpdateExpression="SET #s = :st",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":st": {"S": "active"}},
        )
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": f"Error actualizando inscripción: {e}"}),
        }

    # 2) Recuperar datos de la inscripción
    try:
        resp = dynamodb.get_item(
            TableName=INSCRIPCIONES_TABLE,
            Key={"id": {"S": insc_id}}
        )
        insc = resp.get("Item", {})
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": f"Error leyendo inscripción: {e}"}),
        }

    # 3) Generar hash de la contraseña por defecto
    pwd_plain = "alumno123"
    pwd_hash  = generate_password_hash(pwd_plain)

    # 4) Crear item de usuario
    user_item = {
        "id":            {"S": insc_id},
        "nombre":        {"S": insc.get("studentName", {}).get("S", "")},
        "email":         {"S": insc.get("email", {}).get("S", "")},
        "rol":           {"S": "alumno"},
        "password_hash": {"S": pwd_hash},
    }

    try:
        dynamodb.put_item(
            TableName=USUARIOS_TABLE,
            Item=user_item
        )
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": f"Error creando usuario: {e}"}),
        }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "success": True,
            "message": "Inscripción aprobada y usuario 'alumno' creado con contraseña 'alumno123'."
        }),
    }