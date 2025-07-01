import os
import json
import jwt
from werkzeug.security import check_password_hash
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME       = os.environ["DYNAMODB_TABLE"]   # tabla de usuarios
INDEX_NAME       = os.environ["EMAIL_INDEX"]      # índice secundario sobre "email"
JWT_SECRET       = os.environ["JWT_SECRET"]

def handler(event, context):
    try:
        data = json.loads(event.get("body", "{}"))
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Email y contraseña son requeridos."})
            }

        # 1) Query por email
        resp = DYNAMODB_CLIENT.query(
            TableName=TABLE_NAME,
            IndexName=INDEX_NAME,
            KeyConditionExpression="#e = :email",
            ExpressionAttributeNames={"#e": "email"},
            ExpressionAttributeValues={":email": {"S": email}}
        )
        items = resp.get("Items", [])
        if not items:
            return {
                "statusCode": 401,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Credenciales inválidas."})
            }

        user = items[0]
        stored_hash = user.get("password_hash", {}).get("S", "")

        # 2) Validar contraseña
        if not check_password_hash(stored_hash, password):
            return {
                "statusCode": 401,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Credenciales inválidas."})
            }

        # 3) Preparar payload para JWT
        info = deserialize_item(user)
        info.pop("password_hash", None)

        token = jwt.encode(info, JWT_SECRET, algorithm="HS256")

        # 4) Responder con Set-Cookie para user_session
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Set-Cookie": (
                    f"user_session={token}; "
                    f"Path=/; HttpOnly; SameSite=Lax; Max-Age={60*60*24}"
                )
            },
            "body": json.dumps({
                "message": "Login exitoso",
                "token": token,
                "user": info
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": f"Error interno: {e}"})
        }
