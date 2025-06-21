import os, json, jwt
from utils import get_dynamodb_client, deserialize_item
from werkzeug.security import check_password_hash

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']
INDEX_NAME = os.environ['EMAIL_INDEX']
JWT_SECRET = os.environ['JWT_SECRET']


CORS_HEADERS = {
    "Access-Control-Allow-Origin": "http://localhost:3000",
    "Access-Control-Allow-Credentials": "true"
}

def handler(event, context):
    try:
        data = json.loads(event.get("body", "{}"))
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return {
                "statusCode": 400,
                "headers": CORS_HEADERS,
                "body": json.dumps({"error": "Email y contraseña son requeridos."})
            }

        response = DYNAMODB_CLIENT.query(
            TableName=TABLE_NAME,
            IndexName=INDEX_NAME,
            KeyConditionExpression="email = :email",
            ExpressionAttributeValues={":email": {'S': email}}
        )

        if not response.get('Items'):
            return {
                "statusCode": 401,
                "headers": CORS_HEADERS,
                "body": json.dumps({"error": "Credenciales inválidas."})
            }

        user = response['Items'][0]
        stored_password_hash = user.get('password_hash', {}).get('S')

        if not stored_password_hash or not check_password_hash(stored_password_hash, password):
            return {
                "statusCode": 401,
                "headers": CORS_HEADERS,
                "body": json.dumps({"error": "Credenciales inválidas."})
            }

        user_info = deserialize_item(user)
        user_info.pop('password_hash', None)

        token = jwt.encode(user_info, JWT_SECRET, algorithm="HS256")

        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": json.dumps({"message": "Login exitoso", "token": token})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": CORS_HEADERS,
            "body": json.dumps({"error": f"Error interno: {str(e)}"})
        }
