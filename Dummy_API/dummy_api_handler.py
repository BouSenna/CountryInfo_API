from flask_restful import Resource


class dummyCountryHandler(Resource):

    def req_info(self, country_name):
        return {"name": "Egypt",
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