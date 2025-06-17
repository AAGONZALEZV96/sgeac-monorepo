import os
import boto3

def get_dynamodb_client():
    """Crea y devuelve un cliente de DynamoDB, configurado para LocalStack si es necesario."""
    if os.environ.get('IS_OFFLINE', False):
        return boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
    else:
        return boto3.client("dynamodb")

def deserialize_item(item):
    """Convierte un item de DynamoDB a un diccionario de Python de forma dinámica."""
    if not item:
        return None
        
    deserialized = {}
    for key, val_dict in item.items():
        val_type = list(val_dict.keys())[0]
        value = val_dict[val_type]
        if val_type == 'N':
            try:
                deserialized[key] = int(value)
            except ValueError:
                deserialized[key] = float(value)
        else:
            deserialized[key] = value
    return deserialized