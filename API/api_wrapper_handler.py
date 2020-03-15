from flask_restful import Resource, reqparse
from API.api_handler import countryHandler

class wrapperHandler(Resource):
    def get(self, name):
        country = countryHandler(name)
        country_info = country.req_info()

        parser = reqparse.RequestParser()
        parser.add_argument('info')
        arg = parser.parse_args()

        if arg['info'] == None:
            return country_info
        else:
            for i in country_info:
                if arg['info'] == i:
                    return country_info[i]
            return None
