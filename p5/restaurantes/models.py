from django.db import models
from pymongo import MongoClient
import urllib.request
from bson.json_util import loads
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)    ## Conexión
db = client.test                            ## Base de datos
restaurantes = db.restaurantes              ## Colección

class Restaurantes:
    def loadData(url):
        urljson = urllib.request.urlopen(url)
        for row in urljson:
            jrow = loads(row)
            restaurantes.insert_one(jrow)

    def getByID(_id):
        return restaurantes.find_one({"_id": ObjectId(_id)})

    def getByName(name):
        return restaurantes.find_one({"name": name})

    def getAll():
        return restaurantes.find({})

    def findAndUpdate(_id, update):
        return restaurantes.find_one_and_update({'_id': ObjectId(_id)}, {'$set': update}, projection={'seq':True, '_id':False}, upsert = True)

    def size():
        return restaurantes.count()

    def modifyName(newname):
        return None

    def add(name, coordinates, _type):
        return restaurantes.insert_one({'name': name, 'location':{'coordinates': coordinates, 'type': _type}})
    
    def delByName(name):
        return restaurantes.delete_one({'name': name})

    def delByID(_id):
        return restaurantes.delete_one({'_id': ObjectId(_id)})

    def getIntervalo(min, max):
        datalist = []
        data = Restaurantes.getAll()
        if max > data.count():
            max = data.count()
        for i in range(min, max):
            datalist.append({'_id':str(data[i]['_id']), 'location':data[i]['location'], 'name':data[i]['name']})
        return datalist