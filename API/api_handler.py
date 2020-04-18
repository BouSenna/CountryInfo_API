from flask_restful import Resource
import requests_cache
import requests


class countryHandler(Resource):
    requests_cache.install_cache('cache')

    def req_info(self, country_name):
        path = 'https://restcountries.eu/rest/v2/name/{}'.format(country_name)
        self.response = requests.get(path)

        return self.response.json()[0]

