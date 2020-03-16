import unittest
from API.api_wrapper_handler import wrapperHandler

# in-out dummy interfaces for the Parser and CountryHandler
class dummyParser:
    def __init__(self, o):
        self.o = o
    def parse_args(self):
        return self.o

class dummyCountryHandler:
    def __init__(self, o):
        self.o = o
    def req_info(self, name):
        return self.o
    
class testWrapperHandler(unittest.TestCase):
    def test_invalid_info(self):
        wrapper_handler = wrapperHandler()

        dummy_parser = dummyParser({'info': 'bottomLevelDomain'})
        dummy_country_handler = dummyCountryHandler({"name": "Egypt", "topLevelDomain": ".eg", "capital": "Cairo"})

        wrapper_handler.parser = dummy_parser
        wrapper_handler.country = dummy_country_handler
        
        resp, status_code = wrapper_handler.get('Egypt')
        assert status_code == 400

    def test_valid_info(self):
        wrapper_handler = wrapperHandler()

        dummy_parser = dummyParser({'info': 'topLevelDomain'})
        dummy_country_handler = dummyCountryHandler({"name": "Egypt", "topLevelDomain": ".eg", "capital": "Cairo"})

        wrapper_handler.parser = dummy_parser
        wrapper_handler.country = dummy_country_handler

        resp, status_code = wrapper_handler.get('Egypt')
        assert status_code == 200


if __name__ == '__main__':
    unittest.main()

