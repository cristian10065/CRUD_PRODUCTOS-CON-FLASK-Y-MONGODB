

from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://cristianelianhernandez:Cristian1006532866@cluster0.gkdkseq.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_producto"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db