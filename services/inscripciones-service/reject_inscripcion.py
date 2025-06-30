import os
import json
from utils import get_dynamodb_client

dynamodb = get_dynamodb_client()
TABLE_NAME = os.environ["DYNAMODB_TABLE"]

def handler(event, context):
    # ID extraído de la ruta DELETE /inscripciones/{id}/reject
    insc_id = event["pathParameters"]["id"]

    try:
        dynamodb.delete_item(
            TableName=TABLE_NAME,
            Key={"id": {"S": insc_id}}
        )
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": f"No se pudo eliminar la inscripción: {e}"})
        }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"success": True, "message": "Inscripción eliminada."})
    }