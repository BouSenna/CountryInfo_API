import unittest
import json

from API.api_handler import countryHandler
from API.main import app

class testAPIWrapper(unittest.TestCase):
    def setUp(self):
        self.EG_info = {"name": "Egypt",
                        "topLevelDomain": [
                            ".eg"
                        ],
                        "alpha2Code": "EG",
                        "alpha3Code": "EGY",
                        "callingCodes": [
                            "20"
                        ],
                        "capital": "Cairo",
                        "altSpellings": [
                            "EG",
                            "Arab Republic of Egypt"
                        ],
                        "region": "Africa",
                        "subregion": "Northern Africa",
                        "population": 91290000,
                        "latlng": [
                            27.0,
                            30.0
                        ],
                        "demonym": "Egyptian",
                        "area": 1002450.0,
                        "gini": 30.8,
                        "timezones": [
                            "UTC+02:00"
                        ],
                        "borders": [
                            "ISR",
                            "LBY",
                            "SDN"
                        ],
                        "nativeName": "مصر‎",
                        "numericCode": "818",
                        "currencies": [
                            {
                                "code": "EGP",
                                "name": "Egyptian pound",
                                "symbol": "£"
                            }
                        ],
                        "languages": [
                            {
                                "iso639_1": "ar",
                                "iso639_2": "ara",
                                "name": "Arabic",
                                "nativeName": "العربية"
                            }
                        ],
                        "translations": {
                            "de": "Ägypten",
                            "es": "Egipto",
                            "fr": "Égypte",
                            "ja": "エジプト",
                            "it": "Egitto",
                            "br": "Egito",
                            "pt": "Egipto",
                            "nl": "Egypte",
                            "hr": "Egipat",
                            "fa": "مصر"
                        },
                        "flag": "https://restcountries.eu/data/egy.svg",
                        "regionalBlocs": [
                            {
                                "acronym": "AU",
                                "name": "African Union",
                                "otherAcronyms": [],
                                "otherNames": [
                                    "الاتحاد الأفريقي",
                                    "Union africaine",
                                    "União Africana",
                                    "Unión Africana",
                                    "Umoja wa Afrika"
                                ]
                            },
                            {
                                "acronym": "AL",
                                "name": "Arab League",
                                "otherAcronyms": [],
                                "otherNames": [
                                    "جامعة الدول العربية",
                                    "Jāmiʻat ad-Duwal al-ʻArabīyah",
                                    "League of Arab States"
                                ]
                            }
                        ],
                        "cioc": "EGY"
                        }


    # Requesting all country information
    def test_country_info(self):
        client = app.test_client()
        response = client.get('http://localhost:5000/egypt?')

        self.assertEqual(json.dumps(self.EG_info).encode('UTF-8')+b'\n', response.data)

    # Requesting country name
    def test_country_name(self):
        client = app.test_client()
        response = client.get('http://localhost:5000/egypt?info=name')

        self.assertEqual(b'"Egypt"\n', response.data)

    # Requesting list of currencies
    def test_country_currency(self):
        client = app.test_client()
        response = client.get('http://localhost:5000/egypt?info=currencies')

        self.assertEqual(b'[{"code": "EGP", "name": "Egyptian pound", "symbol": "\u00a3"}]\n', response.data)

    # Requesting missing information
    def test_country_none(self):
        client = app.test_client()
        response = client.get('http://localhost:5000/egypt?info=weather')

        self.assertEqual(b'{"error": "invalid info"}\n', response.data)

    # Requesting cached information.
    def test_country_cachedInfo(self):
        country = countryHandler()
        country.req_info("Iran")
        country.req_info("Iran")

        self.assertTrue(country.response.from_cache)

if __name__ == "__main__":
    unittest.main()
