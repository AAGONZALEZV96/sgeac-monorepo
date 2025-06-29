import os
import json
import boto3
from utils import get_dynamodb_client

# Usamos el cliente configurado para LocalStack o AWS real
dynamodb = get_dynamodb_client()
TABLE_NAME = os.environ.get("DYNAMODB_TABLE")

def handler(event, context):
    cors = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
    # Obtenemos el query param ?status=pending
    status = None
    if event.get("queryStringParameters"):
        status = event["queryStringParameters"].get("status")

    try:
        if status:
            # Filtramos por status usando un nombre de atributo personalizado
            resp = dynamodb.query(
                TableName=TABLE_NAME,
                IndexName="status-index",
                KeyConditionExpression="#st = :s",
                ExpressionAttributeNames={"#st": "status"},
                ExpressionAttributeValues={":s": {"S": status}}
            )
            items = resp.get("Items", [])
        else:
            # Si no hay filtro, listamos todas las inscripciones
            resp = dynamodb.scan(TableName=TABLE_NAME)
            items = resp.get("Items", [])

        # Transformamos cada item de DynamoDB a dict plano
        result = [
            {k: list(v.values())[0] for k, v in item.items()}
            for item in items
        ]

        return {
            "statusCode": 200,
            "headers": cors,
            "body": json.dumps(result)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": cors,
            "body": json.dumps({"message": f"Error interno: {str(e)}"})
        }