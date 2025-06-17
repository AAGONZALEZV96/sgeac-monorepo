import os
import json
import boto3
import pytest
from moto import mock_aws  # <-- CAMBIO 1: La forma de importación más moderna

# Importamos la función 'handler' que queremos probar desde nuestro archivo create.py
from create import handler as create_handler

# --- Configuración de la Prueba (Arrange) ---

@pytest.fixture
def mock_env():
    """Establece las variables de entorno necesarias antes de cada prueba."""
    os.environ['DYNAMODB_TABLE'] = 'tabla-de-prueba-roles'

@mock_aws  # <-- CAMBIO 2: Usamos el decorador general y más robusto
def test_create_rol_success(mock_env):
    """
    Prueba la creación exitosa de un nuevo rol.
    """
    # --- ARRANGE (Preparar) ---
    
    # 1. Creamos una tabla DynamoDB "falsa" en la memoria
    table_name = os.environ['DYNAMODB_TABLE']
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
    )

    # 2. Preparamos un "evento" de API Gateway falso
    test_event = {
        "body": json.dumps({
            "nombre": "Tester"
        })
    }

    # --- ACT (Actuar) ---

    # 3. Ejecutamos nuestra función handler
    response = create_handler(test_event, None)

    # --- ASSERT (Verificar) ---

    # 4. Verificamos la respuesta de la API
    assert response['statusCode'] == 201
    body = json.loads(response['body'])
    assert body['nombre'] == 'Tester'
    assert 'id' in body

    # 5. Verificamos que el dato se haya guardado en la base de datos "falsa"
    get_response = dynamodb.get_item(
        TableName=table_name,
        Key={'id': {'S': body['id']}}
    )
    assert 'Item' in get_response
    assert get_response['Item']['nombre']['S'] == 'Tester'