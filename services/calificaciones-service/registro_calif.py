import os
import json
import uuid
import boto3
from datetime import date

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    # Obtenemos todos los nuevos atributos
    alumno_id = data.get('alumno_id')
    tipo_evaluacion = data.get('tipo_evaluacion') # ej: "NOTA-01"
    descripcion = data.get('descripcion')
    nota = data.get('nota')
    comentarios = data.get('comentarios')

    if not all([alumno_id, tipo_evaluacion, nota is not None]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos: alumno_id, tipo_evaluacion, nota."})}

    calificacion_id = str(uuid.uuid4())
    fecha_hoy = date.today().isoformat()

    item = {
        'id': {'S': calificacion_id},
        'alumno_id': {'S': alumno_id},
        'tipo_evaluacion': {'S': tipo_evaluacion},
        'descripcion': {'S': descripcion or 'N/A'},
        'nota': {'N': str(nota)},
        'comentarios': {'S': comentarios or 'Sin comentarios.'},
        'fecha': {'S': fecha_hoy}
    }
    
    dynamodb_client.put_item(TableName=TABLE_NAME, Item=item)
    return {"statusCode": 201, "body": json.dumps({"message": "Calificación registrada exitosamente.", "id": calificacion_id})}