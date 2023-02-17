from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


def init_db():
    # Define the Base class

    engine = create_engine('postgresql://axione:axione@axione-postgres/axione_database')

    # Create the 'cities' table if it doesn't already exist
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
