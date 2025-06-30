import os
import json
from utils import get_dynamodb_client

dynamodb = get_dynamodb_client()
TABLE_NAME = os.environ.get("DYNAMODB_TABLE")


def handler(event, context):
    cors = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True
    }

    insc_id = event.get("pathParameters", {}).get("id")
    if not insc_id:
        return {"statusCode": 400, "headers": cors, "body": json.dumps({"error": "Falta parámetro id"})}

    try:
        # Leer datos enviados en el body
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return {"statusCode": 400, "headers": cors, "body": json.dumps({"error": "Body inválido"})}

    # Construir expresiones de update dinámicamente
    update_expr = []
    expr_attr_vals = {}
    expr_attr_names = {}
    for idx, (k, v) in enumerate(body.items()):
        placeholder_name = f"#f{idx}"
        placeholder_val  = f":v{idx}"
        update_expr.append(f"{placeholder_name} = {placeholder_val}")
        expr_attr_names[placeholder_name] = k
        expr_attr_vals[placeholder_val] = {"S": str(v)}

    if not update_expr:
        return {"statusCode": 400, "headers": cors, "body": json.dumps({"error": "No hay campos para actualizar"})}

    try:
        dynamodb.update_item(
            TableName=TABLE_NAME,
            Key={"id": {"S": insc_id}},
            UpdateExpression="SET " + ", ".join(update_expr),
            ExpressionAttributeNames=expr_attr_names,
            ExpressionAttributeValues=expr_attr_vals
        )
    except Exception as e:
        return {"statusCode": 500, "headers": cors, "body": json.dumps({"error": f"Error actualizando inscripción: {e}"})}

    return {
        "statusCode": 200,
        "headers": cors,
        "body": json.dumps({"success": True, "message": "Inscripción actualizada correctamente."})
    }