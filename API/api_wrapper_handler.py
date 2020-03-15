from flask_restful import Resource, reqparse
from API.api_handler import countryHandler

class wrapperHandler(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('info')
        self.country = countryHandler()

        
    def get(self, name):
        country_info = self.country.req_info(name)
        
        parser = reqparse.RequestParser()
        parser.add_argument('info')
        arg = parser.parse_args()

        if arg['info'] == None:
            return country_info, 200
        else:
            for i in country_info:
                if arg['info'] == i:
                    return country_info[i], 200
            return None, 400
