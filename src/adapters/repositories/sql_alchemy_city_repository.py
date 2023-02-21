from core.exceptions import UnableToFindCitiesException
from core.models import CityModel
from domain.entities.city import City
from ports.repositories.city_repository import ICityRepository


class SQLAlchemyCityRepository(ICityRepository):
    def __init__(self, session):
        self.session = session

    def save(self, city: City) -> None:
        ...

    def find_all(self, **kwargs) -> list[City]:
        try:
            cities_db = self.session.query(CityModel).filter(
                CityModel.price <= kwargs["price"], CityModel.department == kwargs["department"]).all()
            return [City(c.uuid, c.name, c.department, c.price, c.population, c.note) for c in cities_db]
        except Exception:
            raise UnableToFindCitiesException()
