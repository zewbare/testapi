from flask import Flask
from flask_restful import Api
from resources.emp import Emp

app = Flask(__name__)
api = Api(app)

api.add_resource(Emp, '/emp')

if __name__ == '__main__':
    app.run()