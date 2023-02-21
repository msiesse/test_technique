import dataclasses
from typing import List

import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from core.models import CityModel
from core.random_uuid import random_uuid
from scraping.database import init_db


@dataclasses.dataclass
class CityNote:
    name: str
    note: float
    department: str


def get_city_name(text: str) -> str:
    new_text = text.strip()
    start_index = new_text.find('(')
    return new_text[:start_index - 1]


def get_department(text: str) -> str:
    new_text = text.strip()
    start_index = new_text.find('(')
    end_index = new_text.find(')')
    return new_text[start_index + 1:end_index]


def get_note(text: str) -> float:
    return float(text)


def get_cities_from_page(page: int) -> List[CityNote]:
    response = requests.get(f'https://www.bien-dans-ma-ville.fr/classement-ville-global/?page={page}')
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find('tbody')
    rows = body.find_all('tr')
    cities = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) != 3:
            continue
        city_name = get_city_name(cells[1].text)
        department = get_department(cells[1].text)
        note = get_note(cells[2].text)
        cities.append(CityNote(name=city_name, note=note, department=department))
    return cities


def get_cities_from_website() -> List[CityNote]:
    cities = []
    for page in range(1, 26):
        cities += get_cities_from_page(page)
    return cities


def save_cities_entity_for_db(session: Session, cities: List[CityNote]) -> None:
    for city in cities:
        city_db = CityModel(uuid=random_uuid(), name=city.name, note=city.note, department=city.department)
        session.add(city_db)
    session.commit()


def scraping_notes():
    session = init_db()
    cities = get_cities_from_website()
    save_cities_entity_for_db(session, cities)
    session.close()
