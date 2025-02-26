import pymongo
import certifi

connection_string = "mongodb+srv://nagreenfield:fsdi107@fsdi-107.i8val.mongodb.net/?retryWrites=true&w=majority&appName=FSDI-107"

client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.get_database("organika-ch54")