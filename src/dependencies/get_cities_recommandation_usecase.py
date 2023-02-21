from fastapi import Depends

from dependencies.get_city_repository import get_city_repository
from ports.repositories.city_repository import ICityRepository
from usecases.get_recommandations_of_cities import GetRecommandationsOfCitiesUsecase


def get_cities_recommandation_usecase(city_repository: ICityRepository = Depends(get_city_repository)):
    return GetRecommandationsOfCitiesUsecase(city_repository)