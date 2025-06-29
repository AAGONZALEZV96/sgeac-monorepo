import os
import json
import jwt
from utils import get_dynamodb_client, deserialize_item
from werkzeug.security import check_password_hash

# Inicializa DynamoDB y variables de entorno
DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['EMAIL_INDEX']
JWT_SECRET = os.environ['JWT_SECRET']

def handler(event, context):
    """
    Lambda handler para login de usuario.
    Espera { "email": "...", "password": "..." } en el body (JSON).
    Devuelve { "token": "...", "user": {...} } en caso exitoso.
    """
    try:
        # 1. Parsear body del request
        data = json.loads(event.get("body", "{}"))
        email = data.get('email')
        password = data.get('password')

        # 2. Validar campos requeridos
        if not all([email, password]):
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Email y contraseña son requeridos."})
            }

        # 3. Buscar usuario por email en DynamoDB
        response = DYNAMODB_CLIENT.query(
            TableName=TABLE_NAME,
            IndexName=INDEX_NAME,
            KeyConditionExpression="email = :email",
            ExpressionAttributeValues={":email": {'S': email}}
        )
        items = response.get('Items', [])
        if not items:
            return {
                "statusCode": 401,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Credenciales inválidas."})
            }

        user = items[0]
        stored_password_hash = user.get('password_hash', {}).get('S')

        # 4. Validar contraseña
        if not stored_password_hash or not check_password_hash(stored_password_hash, password):
            return {
                "statusCode": 401,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Credenciales inválidas."})
            }

        # 5. Preparar datos del usuario para el token y la respuesta (nunca enviar el hash)
        user_info = deserialize_item(user)
        user_info.pop('password_hash', None)

        # 6. Crear el token JWT (puedes agregar expires, etc. si quieres)
        token = jwt.encode(user_info, JWT_SECRET, algorithm="HS256")

        # 7. Respuesta exitosa
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Login exitoso",
                "token": token,
                "user": user_info
            })
        }

    except Exception as e:
        # 8. Error inesperado
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": f"Error interno: {str(e)}"})
        }
