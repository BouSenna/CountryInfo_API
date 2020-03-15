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
    
def test_invalid_info():
    wrapper_handler = wrapperHandler()

    dummy_parser = dummyParser({'info': 'bottomLevelDomain'})
    dummy_country_handler = dummyCountryHandler({"name": "Egypt", "topLevelDomain": ".eg", "capital": "Cairo"})

    wrapper_handler.country = dummy_country_handler
    wrapper_handler.parser = dummy_parser

    resp, status_code = wrapper_handler.get('Egypt')
    assert status_code == 400


test_invalid_info()
