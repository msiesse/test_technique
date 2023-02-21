from fastapi import Request, status
from fastapi.responses import JSONResponse

from core.exceptions import UnableToFindCitiesException


async def unable_to_find_cities(request: Request, exc: UnableToFindCitiesException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": f"Something goes wrong, can't find cities, please retry again"}
    )
