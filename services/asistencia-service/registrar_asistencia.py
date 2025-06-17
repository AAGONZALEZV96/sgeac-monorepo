import os, json, uuid, boto3
from datetime import date

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    # Ahora recibimos alumno_id, nivel_id y estado
    alumno_id = data.get('alumno_id')
    nivel_id = data.get('nivel_id')
    estado = data.get('estado') # "presente" o "ausente"
    
    if not all([alumno_id, nivel_id, estado]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos."})}

    asistencia_id = str(uuid.uuid4())
    fecha_hoy = date.today().isoformat()

    item = {
        'id': {'S': asistencia_id},
        'alumno_id': {'S': alumno_id},
        'nivel_id': {'S': nivel_id},
        'fecha': {'S': fecha_hoy},
        'estado': {'S': estado}
    }
    dynamodb_client.put_item(TableName=TABLE_NAME, Item=item)
    return {"statusCode": 201, "body": json.dumps({"message": "Asistencia registrada."})}