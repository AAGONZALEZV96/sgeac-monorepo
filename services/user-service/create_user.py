import os
import json
import uuid
import boto3
import logging

# Configuración del logger para ver logs en CloudWatch (o en la terminal de LocalStack)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configuración de DynamoDB
IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    # Si estamos en modo offline/local, nos conectamos a LocalStack
    dynamodb_client = boto3.client(
        "dynamodb", endpoint_url="http://localhost.localstack.cloud:4566"
    )
else:
    # En un entorno real de AWS, boto3 se configura solo
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    """
    Handler para crear un nuevo usuario.
    Recibe los datos del usuario en el cuerpo de la solicitud.
    """
    try:
        # Cargar los datos del cuerpo de la solicitud (que viene como un string)
        body = json.loads(event.get("body", "{}"))

        # Atributos basados en el documento 
        nombre = body.get('nombre')
        rut = body.get('rut')
        email = body.get('email')
        edad = body.get('edad')
        rol = body.get('rol')
        sucursal = body.get('sucursal')

        # Validación simple de campos requeridos
        if not all([nombre, rut, email, edad, rol, sucursal]):
            logger.error("Error de validación: Faltan campos requeridos.")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Faltan campos requeridos: nombre, rut, email, edad, rol, sucursal."})
            }

        # Generar un ID único para el usuario
        user_id = str(uuid.uuid4())

        # Crear el item para DynamoDB
        item = {
            'id': {'S': user_id},
            'rut': {'S': rut},
            'nombre': {'S': nombre},
            'email': {'S': email},
            'edad': {'N': str(edad)},
            'rol': {'S': rol},
            'sucursal': {'S': sucursal}
        }

        # Guardar el item en la tabla
        dynamodb_client.put_item(TableName=TABLE_NAME, Item=item)

        # Preparar la respuesta de éxito
        response_body = {
            "message": "Usuario creado exitosamente!",
            "userId": user_id,
            "data": body
        }
        logger.info(f"Usuario creado con ID: {user_id}")
        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response_body)
        }

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Ocurrió un error interno en el servidor."})
        }