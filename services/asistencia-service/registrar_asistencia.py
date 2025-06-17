import os, json, uuid
from datetime import date
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    alumno_id = data.get('alumno_id')
    nivel_id = data.get('nivel_id')
    estado = data.get('estado')

    if not all([alumno_id, nivel_id, estado]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos."})}

    item = {
        'id': {'S': str(uuid.uuid4())},
        'alumno_id': {'S': alumno_id},
        'nivel_id': {'S': nivel_id},
        'fecha': {'S': date.today().isoformat()},
        'estado': {'S': estado}
    }
    
    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    return {"statusCode": 201, "body": json.dumps({"message": "Asistencia registrada."})}