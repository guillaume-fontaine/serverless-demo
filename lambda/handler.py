#comm
import json
import boto3
import os

def handler(event, context):
    # Sécurisé : lecture dynamique de la variable d’environnement
    table_name = os.environ.get("TABLE_NAME")

    if not table_name:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "TABLE_NAME not set"})
        }

    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-east-1',
        endpoint_url='http://ip10-0-6-5-cvhtafqb9qb14bivkpqg-4566.direct.lab-boris.fr',
        aws_access_key_id='test',
        aws_secret_access_key='test'
    )

    table = dynamodb.Table(table_name)

    route = event.get("rawPath", "")
    method = event.get("requestContext", {}).get("http", {}).get("method", "")

    if route == "/hello" and method == "GET":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Hello from Lambda!"})
        }

    elif route == "/contact" and method == "POST":
        body = json.loads(event.get("body", "{}"))
        item = {
            "email": body.get("email"),
            "name": body.get("name"),
            "message": body.get("message")
        }
        table.put_item(Item=item)
        return {
            "statusCode": 200,
            "body": json.dumps({"status": "saved"})
        }

    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Not found"})
        }
