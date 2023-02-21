from fastapi import Depends
from sqlalchemy.orm import Session

from adapters.repositories.sql_alchemy_city_repository import SQLAlchemyCityRepository
from dependencies.get_db import get_db


def get_city_repository(session: Session = Depends(get_db)):
   return SQLAlchemyCityRepository(session)