from flask_restful import Resource

class WelcomeController(Resource):
    def get(self):
        return {'welcome': "welcome, stranger!"}