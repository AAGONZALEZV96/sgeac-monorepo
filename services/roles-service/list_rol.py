import os
import json
from utils import get_dynamodb_client, deserialize_item

# Inicializamos el cliente una sola vez usando nuestra función de utilidades
DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    """
    Handler refactorizado para listar todos los roles.
    Usa la función deserialize_item importada desde utils.
    """
    try:
        response = DYNAMODB_CLIENT.scan(TableName=TABLE_NAME)
        
        # Usamos la función de deserialización centralizada
        items = [deserialize_item(item) for item in response.get('Items', [])]
        
        return {
            "statusCode": 200,
            "body": json.dumps(items)
        }
    except Exception as e:
        # Es una buena práctica añadir manejo de errores también aquí
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Error interno del servidor: {str(e)}"})
        }