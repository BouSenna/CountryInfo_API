from flask_restful import Resource, reqparse
from api_handler import countryHandler

class wrapperHandler(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('info')
        self.country = countryHandler()
        self.invalid_info = {'error': 'invalid info'}, 400
        super().__init__()

        
    def get(self, name):
        country_info = self.country.req_info(name)
        arg = self.parser.parse_args()

        # If no specific arguments were specified, dump everything.
        if arg['info'] == None:
            return country_info, 200
        # Else, if specified info was found, return it with success code, if not then return invalid with 400 code.
        else:
            for i in country_info:
                if arg['info'] == i:
                    return country_info[i], 200
            return self.invalid_info
