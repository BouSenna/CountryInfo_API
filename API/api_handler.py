from flask_restful import Resource
import requests

class countryHandler(Resource):
    def __init__(self, name):
        self.country_name = name

    def req_info(self):
        path = 'https://restcountries.eu/rest/v2/name/{}'.format(self.country_name)
        response = requests.get(path)
        return response.json()[0]

