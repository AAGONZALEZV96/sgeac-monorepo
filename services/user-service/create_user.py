import os
import json
import uuid
from utils import get_dynamodb_client
from werkzeug.security import generate_password_hash

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    try:
        data = json.loads(event.get("body", "{}"))
        
        # --- Campos requeridos ---
        email = data.get('email')
        password = data.get('password')
        nombre = data.get('nombre')
        rol = data.get('rol')

        if not all([email, password, nombre, rol]):
            return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos: email, password, nombre, rol."})}

        password_hash = generate_password_hash(password)
        user_id = str(uuid.uuid4())
        
        # --- Construcción del item de forma dinámica ---
        # 1. Empezamos con los campos que siempre estarán
        item = {
            'id': {'S': user_id},
            'email': {'S': email},
            'password_hash': {'S': password_hash},
            'nombre': {'S': nombre},
            'rol': {'S': rol},
        }

        # 2. Añadimos los campos opcionales SOLO SI existen en los datos recibidos
        if data.get('rut'):
            item['rut'] = {'S': data.get('rut')}
        if data.get('edad'):
            item['edad'] = {'N': str(data.get('edad'))}
        if data.get('telefono'):
            item['telefono'] = {'S': data.get('telefono')}
        if data.get('direccion'):
            item['direccion'] = {'S': data.get('direccion')}
        if data.get('sucursal_asignada'):
            item['sucursal_asignada'] = {'S': data.get('sucursal_asignada')}
        # ----------------------------------------------
        
        DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
        
        # Preparamos la respuesta para el auto-login (como lo habíamos diseñado)
        # ... (puedes añadir aquí la lógica del token JWT si lo deseas) ...
        
        return {"statusCode": 201, "body": json.dumps({"message": "Usuario creado exitosamente."})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": f"Error interno: {str(e)}"}) }