import os
import json
from utils import get_dynamodb_client, deserialize_item

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    user_id = event['pathParameters']['id']
    try:
        # Parsear body
        data = json.loads(event.get('body', '{}'))
        if not data:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'El cuerpo de la petición no puede estar vacío.'})
            }

        update_expression_parts = []
        expression_attribute_values = {}

        for key, value in data.items():
            # No permitimos actualizar la clave primaria
            if key == 'id':
                continue
            # Omitir valores nulos o cadenas vacías
            if value is None or (isinstance(value, str) and value.strip() == ''):
                continue

            # Manejar actualización de contraseña
            if key == 'password':
                from werkzeug.security import generate_password_hash
                hashed = generate_password_hash(value)
                update_expression_parts.append('password_hash = :password_hash')
                expression_attribute_values[':password_hash'] = {'S': hashed}
                continue

            # Para todos los demás campos, tratarlos como string, incluyendo 'edad'
            update_expression_parts.append(f"{key} = :{key}")
            expression_attribute_values[f":{key}"] = {'S': str(value)}

        if not update_expression_parts:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No hay campos válidos para actualizar.'})
            }

        update_expression = 'SET ' + ', '.join(update_expression_parts)

        # Ejecutar actualización en DynamoDB
        response = DYNAMODB_CLIENT.update_item(
            TableName=TABLE_NAME,
            Key={'id': {'S': user_id}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues='ALL_NEW'
        )

        # Construir respuesta sin el hash de contraseña
        updated_item = deserialize_item(response['Attributes'])
        updated_item.pop('password_hash', None)

        return {
            'statusCode': 200,
            'body': json.dumps(updated_item)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Error interno: {str(e)}'})
        }
