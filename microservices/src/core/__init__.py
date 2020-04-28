import os
from pymongo import MongoClient
from src.aws_services.aws_secrets_manager import AwsSecretsManager
from .config import Config

# Get MongoURI from AWS credentials
aws_secrets_manager = AwsSecretsManager()
secrets = aws_secrets_manager.get_secret(os.environ['APP_CONFIG'])
config = Config(secrets)

# Connect to database
mongo_uri = config.MONGO_URI
if not mongo_uri:
    raise Exception('MONGO_URI environment variable not found.')

client = MongoClient(mongo_uri)
db = client.database_name
