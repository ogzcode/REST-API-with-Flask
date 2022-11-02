from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

class Colors(Resource):
    def get(self):
        rgb = [random.randint(0,255) for i in range(3)]

        return {"rgb": rgb}, 200

api.add_resource(Colors, "/colors")

if __name__ == "__main__":
    app.run()

