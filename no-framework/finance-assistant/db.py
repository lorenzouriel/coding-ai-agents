from sqlmodel import SQLModel, create_engine, Session
from models import Transaction

sqlite_file_name = "database_db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)