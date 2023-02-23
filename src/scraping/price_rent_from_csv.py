import csv
import dataclasses
import os
from typing import List, Tuple

from sqlalchemy import func
from sqlalchemy.orm import Session
from tqdm import tqdm

from core.models import CityModel
from scraping.database import init_db


@dataclasses.dataclass
class CityWithRentPrice:
    name: str
    rent_price: float


particularities = {
    "Courcouronnes": "Évry-Courcouronnes",
    "Paris 1er Arrondissement": "Paris",
    "Marseille 1er Arrondissement": "Marseille",
    "Lyon 1er Arrondissement": "Lyon",
    "Herblay": "Herblay-sur-Seine",
    "Le Chesnay": "Le Chesnay-Rocquencourt",
}

current_dir = os.path.dirname(os.path.abspath(__file__))


def update_cities_entites_for_db(session: Session, cities: List[CityWithRentPrice]) -> None:
    for city in cities:
        city_db = session.query(CityModel).filter(func.lower(CityModel.name) == city.name.lower()).first()
        if city_db:
            city_db.price = city.rent_price
    session.commit()


def get_cities_from_csv() -> List[CityWithRentPrice]:
    cities = []
    with open(f'{current_dir}/assets/indicateurs-loyers-maisons.csv', 'r', encoding='latin-1', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            city_department, city_name, rent_price = get_data_from_row(row)
            city_name = update_particularities(city_department, city_name)
            city = CityWithRentPrice(name=city_name, rent_price=rent_price)
            cities.append(city)
    return cities


def get_data_from_row(row) -> Tuple[str, str, float]:
    city_name = row[2]
    city_department = row[3]
    rent_price = float(row[7].replace(',', '.'))
    return city_department, city_name, rent_price


def update_particularities(city_department, city_name) -> str:
    if city_name == "Saint-Ouen" and city_department == "93":
        return "Saint-Ouen-sur-Seine"
    elif city_name in particularities.keys():
        return particularities[city_name]
    return city_name


def save_square_meter_rent_price():
    session = init_db()
    cities = get_cities_from_csv()
    update_cities_entites_for_db(session, cities)
    session.close()
