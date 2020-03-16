import flask
from flask_restful import Api
from api_wrapper_handler import wrapperHandler

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(wrapperHandler, '/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
