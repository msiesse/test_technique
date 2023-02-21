from domain.entities.city import City
from ports.repositories.city_repository import ICityRepository
from usecases.dtos import RecommandationsOptionsDTO


class GetRecommandationsOfCitiesUsecase:
    def __init__(self, city_repository: ICityRepository):
        self.city_repository = city_repository

    def __call__(self, options: RecommandationsOptionsDTO) -> list[City]:
        return self.city_repository.find_all(price=options.price/options.surface, department=options.department)
