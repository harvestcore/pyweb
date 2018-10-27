from pymongo import MongoClient
import urllib.request
from bson.json_util import loads
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)    ## Conexión
dbmongo = client.practica4                  ## Base de datos
restaurantes = dbmongo.practica4            ## Colección


class DBRestaurantes:
    def loadData(url):
        urljson = urllib.request.urlopen(url)
        for row in urljson:
            jrow = loads(row)
            restaurantes.insert_one(jrow)

    def getByID(_id):
        document = restaurantes.find_one({"_id": _id})
        return document

    def getByName(name):
        document = restaurantes.find_one({"name": name})
        return document

    def getAll():
        return restaurantes.find({})

    def getIntervalo(min, max):
        datalist = []
        data = DBRestaurantes.getAll()
        for i in range(min, max):
            datalist.append({'_id':str(data[i]['_id']), 'location':data[i]['location'], 'name':data[i]['name']})


