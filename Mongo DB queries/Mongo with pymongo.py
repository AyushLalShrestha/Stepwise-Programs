from pymongo import MongoClient

#client = MongoClient()  //i.e localhost:27017
client = MongoClient("mongodb://mongodb0.example.net:27017")

db = client['primer']  #db = client.primer //To assign the database named primer to the local variable db

coll = db['dataset']  #coll = db.dataset //Grabbing a Collection(table) named dataset







