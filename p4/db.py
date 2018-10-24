from pymongo import MongoClient
import urllib.request
from bson.json_util import loads
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)    ## Conexión
dbmongo = client.practica4                  ## Base de datos
restaurantes = dbmongo.practica4            ## Colección


class dbmongo:
    def loadData(url):
        urljson = urllib.request.urlopen(url)
        for row in urljson:
            jrow = loads(row)
            restaurantes.insert_one(jrow)

    def get(namexd):
        document = restaurantes.find_one({"name": namexd})
        return document

    def getAll():
        return restaurantes.find({})



