# connection.py
from pymongo import MongoClient

class Database():

    def __init__(self):
        self.client = MongoClient("mongodb://metabus:metabus@43.201.165.100:27017/")
        self.db = "myDatabase"
        self.collection = "myCollectionTwo"
    
    def get_connection(self):
        client = self.client
        db = client[self.db]
        database_collection = db[self.collection]

        return database_collection