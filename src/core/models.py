from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# Define the CityModel class that maps to the 'cities' table
class CityModel(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36))
    name = Column(String(255))
    department = Column(String(255))
    price = Column(Float)
    population = Column(Integer)
    note = Column(Float)
