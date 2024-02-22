import os
from pymongo.mongo_client import MongoClient

os.load_dotenv()
MONGO_API_URI = os.getenv('MONGO_API_URI')

# Create a new client and connect to the server
client = MongoClient(MONGO_API_URI)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)