import os
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

load_dotenv()

database_uri = os.environ['DATABASE_CONNECTION']

client = MongoClient(database_uri, server_api=ServerApi('1'))

database = client[os.environ['CLUSTER_DB']]