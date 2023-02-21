from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_db():
    engine = create_engine('postgresql://axione:axione@axione-postgres/axione_database')
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()
