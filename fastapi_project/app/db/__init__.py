from .session import get_db, engine, Base
from app.models import student, group

def create_tables():
    Base.metadata.create_all(bind=engine)