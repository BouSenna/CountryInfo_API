import unittest
from API.api_handler import countryHandler

class testCountryHandler(unittest.TestCase):
    def setUp(self):
        self.dict_keys = ['name', 'topLevelDomain', 'alpha2Code', 'alpha3Code', 'callingCodes''', 'capital', 'altSpellings', 'region',
                          'subregion', 'population', 'latlng', 'demonym', 'area', 'gini', 'timezones', 'borders', 'nativeName',
                          'numericCode', 'currencies', 'languages', 'translations', 'flag', 'regionalBlocs', 'cioc']

    def test_reqinfo(self):
        country = countryHandler()
        country_info = country.req_info('Egypt')

        assert isinstance(country_info, dict)
        assert set(self.dict_keys).issubset(country_info.keys())


if __name__ == '__main__':
    unittest.main()
