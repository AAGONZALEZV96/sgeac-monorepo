import os, json, uuid
from datetime import date
from utils import get_dynamodb_client

DYNAMODB_CLIENT = get_dynamodb_client()
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    alumno_id = data.get('alumno_id')
    tipo_evaluacion = data.get('tipo_evaluacion')
    nota = data.get('nota')

    if not all([alumno_id, tipo_evaluacion, nota is not None]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos."})}

    item = {
        'id': {'S': str(uuid.uuid4())},
        'alumno_id': {'S': alumno_id},
        'tipo_evaluacion': {'S': tipo_evaluacion},
        'descripcion': {'S': data.get('descripcion', 'N/A')},
        'nota': {'N': str(nota)},
        'comentarios': {'S': data.get('comentarios', 'Sin comentarios.')},
        'fecha': {'S': date.today().isoformat()}
    }
    
    DYNAMODB_CLIENT.put_item(TableName=TABLE_NAME, Item=item)
    return {"statusCode": 201, "body": json.dumps({"message": "Calificación registrada exitosamente.", "id": item['id']['S']})}