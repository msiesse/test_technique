from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.models import Base


def init_db():
    # Define the Base class

    engine = create_engine('postgresql://axione:axione@axione-postgres/axione_database')

    # Create the 'cities' table if it doesn't already exist
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
