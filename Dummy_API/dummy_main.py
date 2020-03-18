import flask
from flask_restful import Api
from Dummy_API.dummy_api_wrapper_handler import dummyWrapperHandler

dummy_app = flask.Flask(__name__)
dummy_api = Api(dummy_app)

dummy_api.add_resource(dummyWrapperHandler, '/<string:name>')

if __name__ == '__main__':
    dummy_app.run(debug=True)
