from pymongo import MongoClient

client = MongoClient("mongodb://43.201.165.100:27017/")
db = client["myDatabase"]
bus_database = db["myCollection"]

print(client)