from domain.entities.city import City
from ports.repositories.city_repository import ICityRepository


class FakeInMemoryCityRepository(ICityRepository):
    def __init__(self):
        self.cities: dict[str, City] = {}

    def save(self, city: City) -> None:
        self.cities[city.uuid] = city

    def find_all(self, **kwargs) -> list[City]:
        return [city for city in self.cities.values() if
                city.price <= kwargs["price"] and city.department == kwargs["department"]]
