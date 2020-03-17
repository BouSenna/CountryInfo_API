import unittest
from Dummy_API.dummy_api_handler import dummyCountryHandler

class testCountryHandler(unittest.TestCase):
    def setUp(self):
        self.dict_keys = ['name', 'topLevelDomain', 'alpha2Code', 'alpha3Code', 'callingCodes''', 'capital', 'altSpellings', 'region',
                          'subregion', 'population', 'latlng', 'demonym', 'area', 'gini', 'timezones', 'borders', 'nativeName',
                          'numericCode', 'currencies', 'languages', 'translations', 'flag', 'regionalBlocs', 'cioc']

    def test_reqinfo_return_type(self):
        country = dummyCountryHandler()
        country_info = country.req_info('Egypt')

        # asserts that req_info returns a dictionary.
        assert isinstance(country_info, dict)

    def test_reqinfo_data_completeness(self):
        country = dummyCountryHandler()
        country_info = country.req_info('Egypt')

        # asserts that the country_info dictionary contains all the dict_keys.
        assert set(self.dict_keys).issubset(country_info.keys())

    def test_reqinfo_return_values(self):
        country = dummyCountryHandler()
        country_info = country.req_info('Egypt')

        # asserts that the values of the country_info is correct.
        assert country_info['name'] == 'Egypt'


if __name__ == '__main__':
    unittest.main()