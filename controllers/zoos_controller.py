from sqlalchemy.sql.expression import select
from ..database import Session
from flask_restful import Resource
from ..models.zoo import Zoo
from flask import request
from flask import jsonify

class ZoosController(Resource):

    # listar zoologicos
    def get(self):
        zoos = select(Zoo)
        return jsonify(zoos)

    # crear zoologico
    def post(self):
        session = Session()

        # payload
        data = request.json

        zoo = Zoo()
        zoo.nombre = data["nombre"]
        zoo.ciudad = data["ciudad"]
        zoo.tamano_m2 = data["tamano_m2"]
        zoo.presupuesto_anual = data["presupuesto_anual"]

        session.add(zoo)
        session.commit()

        return "OK", 201



        