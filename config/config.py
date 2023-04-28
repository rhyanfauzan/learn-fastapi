from pymongo.mongo_client import MongoClient

# Mongo DB --- ***
uri = "mongodb+srv://ujangeneng69:ragSeJpMxQJmp22f@ujang.vjftncz.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection

db = client.get_database("learn-fastapi")

def get_db_connection():
    return db
# End Mongo DB --- ***