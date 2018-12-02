from django.db import models
from pymongo import MongoClient
import urllib.request
from django.core.exceptions import ValidationError
from bson.json_util import loads
from bson.objectid import ObjectId

from mongoengine import *

connect(db='test')

class RestaurantesMongo(Document):
    _id = ObjectIdField()
    location = PointField()
    name = StringField(max_length=50, required=True)


client = MongoClient('localhost', 27017)    ## Conexión
db = client.test                            ## Base de datos
restaurantes = db.restaurantes              ## Colección


class Plato(models.Model):
    chef = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    tipoCocina = models.CharField(max_length = 50)
    alergenos = models.CharField(max_length = 150)
    precio = models.FloatField()
    nombre = models.CharField(max_length = 150)
    descripccion = models.TextField()
    ingredientes = models.TextField()

    def clean(self):
        if self.precio < 0.0 or self.precio == '':
            raise ValidationError('El precio del plato no puede ser menor que 0.')

        if self.nombre == '':
            raise ValidationError('El plato debe tener un nombre.')

        if self.tipoCocina == '':
            raise ValidationError('El plato debe pertenecer a un tipo de cocina.')

        if self.ingredientes == '':
            raise ValidationError('El plato debe tener ingredientes.')

    def add(self):
        self.save()

    def __str__(self):
        return self.nombre


class Restaurantes:
    def loadData(url):
        urljson = urllib.request.urlopen(url)
        for row in urljson:
            jrow = loads(row)
            restaurantes.insert_one(jrow)

    def getByID(_id):
        r = restaurantes.find_one({"_id": ObjectId(_id)})
        rest = {
                'name': r['name'],
                'id': str(r['_id']),
                'location': r['location']
            }
        return rest

    def getByName(name):
        r = restaurantes.find_one({"name": name})
        rest = {
                'name': r['name'],
                'id': str(r['_id']),
                'location': r['location']
            }

        return rest

    def getListByName(name):
        rest = restaurantes.find({"name": { "$regex": ".*" + name + ".*", "$options": "-i" } })
        lst = []

        for r in rest:
            lst.append({
                'name': r['name'],
                'id': str(r['_id']),
                'location': r['location']
            })

        return lst

    def getListByID(_id):
        lst = []
        lst.append(Restaurantes.getByID(_id))

        return lst

    def getAll():
        rest = restaurantes.find({})
        lst = []

        for r in rest:
            lst.append({
                'name': r['name'],
                'id': str(r['_id']),
                'location': r['location']
            })
        
        return lst
        

    def findAndUpdate(_id, update):
        return restaurantes.find_one_and_update({'_id': ObjectId(str(_id))}, {'$set': update}, projection={'seq':True, '_id':False}, upsert = True)

    def size():
        return restaurantes.count()

    def modifyName(newname):
        return None

    def add(name, coordinates, _type):
        return restaurantes.insert_one({'name': name, 'location':{'coordinates': coordinates, 'type': _type}})
    
    def delByName(name):
        return restaurantes.delete_one({'name': name})

    def delByID(_id):
        return restaurantes.delete_one({'_id': ObjectId(str(_id))})

    def getIntervalo(min, max):
        datalist = []
        data = Restaurantes.getAll()
        if max > data.count():
            max = data.count()
        for i in range(min, max):
            datalist.append({'_id':str(data[i]['_id']), 'location':data[i]['location'], 'name':data[i]['name']})
        return datalist