# Environment variables
import os
from dotenv import load_dotenv

load_dotenv()
HOST     = os.getenv("HOST")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
DB_NAME = os.getenv("DB_NAME")


# SQLAlchemy and database session configuration
from sqlalchemy.orm             import Session
from sqlalchemy                 import create_engine

DATABASE_URL = f"mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL, future=True)

def get_session() -> Session:
    try:
        return Session(engine)
    except Exception as e:
        raise ConnectionError(f'Error en la conexión a la base de datos {e}')

