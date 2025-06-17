# services/material-academico-service/create.py
import os, json, uuid, boto3

IS_OFFLINE = os.environ.get('IS_OFFLINE', False)
if IS_OFFLINE:
    dynamodb_client = boto3.client("dynamodb", endpoint_url="http://localhost.localstack.cloud:4566")
else:
    dynamodb_client = boto3.client("dynamodb")

TABLE_NAME = os.environ['DYNAMODB_TABLE']

def handler(event, context):
    data = json.loads(event.get("body", "{}"))
    
    # Atributos del material, incluyendo el ID del nivel al que pertenece
    nivel_id = data.get('nivel_id')
    nombre = data.get('nombre')
    tipo_archivo = data.get('tipo_archivo') # Ej: "PDF", "Video", "Imagen" 
    enlace_descarga = data.get('enlace_descarga') # Ej: URL a un Google Drive, S3, etc. 

    if not all([nivel_id, nombre, tipo_archivo, enlace_descarga]):
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan atributos requeridos."})}

    material_id = str(uuid.uuid4())

    item = {
        'id': {'S': material_id},
        'nivel_id': {'S': nivel_id},
        'nombre': {'S': nombre},
        'tipo_archivo': {'S': tipo_archivo},
        'enlace_descarga': {'S': enlace_descarga}
    }
    
    dynamodb_client.put_item(TableName=TABLE_NAME, Item=item)
    
    # Deserializamos el item para devolverlo limpio
    response_body = {key: val['S'] for key, val in item.items()}
    
    return {"statusCode": 201, "body": json.dumps(response_body)}