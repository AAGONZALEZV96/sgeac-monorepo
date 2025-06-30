import os
import json
import uuid
from utils import get_dynamodb_client
from werkzeug.security import generate_password_hash

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ["DYNAMODB_TABLE"]

def handler(event, context):
    cors = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }

    try:
        data = json.loads(event.get("body", "{}"))

        # Campos obligatorios
        email    = data.get("email")
        password = data.get("password")
        nombre   = data.get("nombre")
        rol      = data.get("rol")

        if not all([email, password, nombre, rol]):
            return {
                "statusCode": 400,
                "headers": cors,
                "body": json.dumps({
                    "success": False,
                    "message": "Faltan atributos requeridos: email, password, nombre, rol."
                })
            }

        # Campos adicionales
        phone        = data.get("phone", "")
        edad         = data.get("edad")          # número
        clase        = data.get("clase", "")
        info_medica  = data.get("info_medica", "")
        experiencia  = data.get("experiencia", "")
        horario      = data.get("horario", "")

        # Hashear contraseña
        password_hash = generate_password_hash(password)
        user_id       = str(uuid.uuid4())

        # Construcción dinámica del item
        item = {
            "id":            {"S": user_id},
            "email":         {"S": email},
            "nombre":        {"S": nombre},
            "rol":           {"S": rol},
            "password_hash": {"S": password_hash},
        }

        # Campos opcionales
        if phone:
            item["phone"] = {"S": phone}
        if isinstance(edad, (int, float, str)) and str(edad).isdigit():
            item["edad"] = {"N": str(edad)}
        if clase:
            item["clase"] = {"S": clase}
        if info_medica:
            item["info_medica"] = {"S": info_medica}
        if experiencia:
            item["experiencia"] = {"S": experiencia}
        if horario:
            item["horario"] = {"S": horario}

        # Inserción en DynamoDB
        DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)

        return {
            "statusCode": 201,
            "headers": cors,
            "body": json.dumps({"success": True, "message": "Usuario creado exitosamente."})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors,
            "body": json.dumps({"success": False, "message": f"Error interno: {str(e)}"})
        }
