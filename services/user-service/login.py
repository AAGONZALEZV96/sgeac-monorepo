import os
import json
import jwt
from utils import get_dynamodb_client, deserialize_item
from werkzeug.security import check_password_hash

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['EMAIL_INDEX']
JWT_SECRET = os.environ['JWT_SECRET']

def handler(event, context):
    try:
        data = json.loads(event.get("body", "{}"))
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return {"statusCode": 400, "body": json.dumps({"error": "Email y contraseña son requeridos."})}

        # Buscamos al usuario por su email usando el índice
        response = DYNAMODB_CLIENT.query(
            TableName=TABLE_NAME,
            IndexName=INDEX_NAME,
            KeyConditionExpression="email = :email",
            ExpressionAttributeValues={":email": {'S': email}}
        )

        if not response.get('Items'):
            return {"statusCode": 401, "body": json.dumps({"error": "Credenciales inválidas."})}

        user = response['Items'][0]
        stored_password_hash = user.get('password_hash', {}).get('S')

        # Verificamos si la contraseña enviada coincide con el hash guardado
        if not stored_password_hash or not check_password_hash(stored_password_hash, password):
            return {"statusCode": 401, "body": json.dumps({"error": "Credenciales inválidas."})}
        
        # --- LÓGICA CORREGIDA ---
        # 1. Preparamos la información del usuario para el token y la respuesta
        user_info = deserialize_item(user)
        user_info.pop('password_hash', None) # ¡Importante! Nunca incluir el hash

        # 2. Creamos el token
        token = jwt.encode(user_info, JWT_SECRET, algorithm="HS256")

        # 3. Devolvemos una respuesta que INCLUYE el objeto 'user'
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Login exitoso", 
                "token": token,
                "user": user_info # <-- ESTA ES LA CLAVE QUE FALTABA EN LA RESPUESTA
            })
        }
    
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": f"Error interno: {str(e)}"}) }