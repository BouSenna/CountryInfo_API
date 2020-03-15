from flask_restful import Resource
import requests

class countryHandler(Resource):

    def req_info(self, country_name):
        path = 'https://restcountries.eu/rest/v2/name/{}'.format(self.country_name)
        response = requests.get(path)
        return response.json()[0]

