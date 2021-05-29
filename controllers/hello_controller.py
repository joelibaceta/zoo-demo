from flask_restful import Resource

class HelloController(Resource):

    def get(self):
        return "hello world"