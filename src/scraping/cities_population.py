import dataclasses

import requests

from core.models import CityModel
from scraping.database import init_db


@dataclasses.dataclass
class CityWithPopulation:
    uuid: str
    name: str
    department: str
    population: int


@dataclasses.dataclass
class CityWithoutPopulation:
    uuid: str
    name: str
    department: str


def get_all_cities_without_population_from_db(cities_db: list[CityModel]) -> list[CityWithoutPopulation]:
    return [CityWithoutPopulation(city_db.uuid, city_db.name, city_db.department) for city_db in cities_db]


def get_cities_with_population(cities_without_population: list[CityWithoutPopulation]) -> list[CityWithPopulation]:
    cities = []
    for city in cities_without_population:
        result = requests.get(
            f"https://geo.api.gouv.fr/communes?nom={city.name}&codeDepartement={city.department}&fields=population&format=json")
        cities.append(CityWithPopulation(city.uuid, city.name, city.department, result.json()[0]["population"]))
    return cities


def save_cities_population():
    session = init_db()
    cities_db = session.query(CityModel).all()
    cities_without_population = get_all_cities_without_population_from_db(cities_db)
    cities_with_population = get_cities_with_population(cities_without_population)
    for i in range(len(cities_db)):
        cities_db[i].population = cities_with_population[i].population
    session.commit()
    session.close()
