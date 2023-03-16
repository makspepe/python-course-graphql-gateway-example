import json
import os

from models.countries import CountryModel


class CountriesService:
    """
    Сервис для работы с данными о странах.
    """

    @staticmethod
    def get_countries() -> list[CountryModel]:
        """
        Получение списка стран.

        :return:
        """

        result = []
        countries_file = "fixtures/countries.json"
        base_dir = os.path.dirname(os.path.dirname(__file__))
        countries_file = os.path.join(base_dir, countries_file)
        with open(countries_file, encoding="utf-8") as file:
            if data := json.load(file):
                result = [
                    CountryModel(
                        name=country.get("name"),
                        alpha2code=country.get("alpha2code"),
                        alpha3code=country.get("alpha3code"),
                        capital=country.get("capital"),
                        region=country.get("region"),
                        subregion=country.get("subregion"),
                        population=country.get("population"),
                        latitude=country.get("latitude"),
                        longitude=country.get("longitude"),
                        demonym=country.get("demonym"),
                        area=country.get("area"),
                        numeric_code=country.get("numeric_code"),
                        flag=country.get("flag"),
                        currencies=country.get("currencies"),
                        languages=country.get("languages"),
                    )
                    for country in data
                ]

        return result
