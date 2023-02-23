from fastapi import FastAPI, Depends, Query

from api.handlers import unable_to_find_cities
from core.exceptions import UnableToFindCitiesException
from dependencies.get_cities_recommandation_usecase import get_cities_recommandation_usecase
from domain.entities.city import City
from usecases.dtos import RecommandationsOptionsDTO
from usecases.get_recommandations_of_cities import GetRecommandationsOfCitiesUsecase

app = FastAPI()
app.add_exception_handler(UnableToFindCitiesException, unable_to_find_cities)


@app.get("/", response_model=list[City])
async def get_cities_recommandations(
        department: str = Query(default="75", description="Code of the department"),
        price: int = Query(default=0, description="Price of the entire rent in euros"),
        surface: int = Query(gt=0, default=1, description="Surface in squared meters"),
        recommandation_usecase: GetRecommandationsOfCitiesUsecase = Depends(get_cities_recommandation_usecase)
):
    return recommandation_usecase(RecommandationsOptionsDTO(department, surface, price))
