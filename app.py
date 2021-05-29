
from .controllers.zoo_animal_controller import ZooAnimalController
from .controllers.hello_controller import HelloController
from .controllers.zoos_controller import ZoosController
from .controllers.zoo_animals_controller import ZooAnimalsController 

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloController,'/hello')
api.add_resource(ZoosController,'/zoos')
api.add_resource(ZooAnimalsController,'/zoo/<int:zoo_id>/animals')
api.add_resource(ZooAnimalController,'/zoo/<int:zoo_id>/animal/<int:animal_id>')

# /especies POST GET
# /especie/<especie_id>/animals
# /especie/<especie_id>/animal/<animal_id>