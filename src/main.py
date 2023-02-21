from fastapi import FastAPI, Depends, Query

from api.handlers import unable_to_find_cities
from core.exceptions import UnableToFindCitiesException
from dependencies.get_cities_recommandation_usecase import get_cities_recommandation_usecase
from usecases.dtos import RecommandationsOptionsDTO
from usecases.get_recommandations_of_cities import GetRecommandationsOfCitiesUsecase

app = FastAPI()
app.add_exception_handler(UnableToFindCitiesException, unable_to_find_cities)


@app.get("/")
async def get_cities_recommandations(
        department: str = "75",
        price: int = 0,
        surface: int = Query(gt=0),
        recommandation_usecase: GetRecommandationsOfCitiesUsecase = Depends(get_cities_recommandation_usecase)
):
    return recommandation_usecase(RecommandationsOptionsDTO(department, surface, price))
