from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base
from api.models import DynamicData

# Base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_database_connection():
    db = TestingSessionLocal()
    assert db is not None

def test_insert_data():
    db = TestingSessionLocal()
    Base.metadata.create_all(bind=engine)
    
    new_entry = DynamicData(data={"name": "Alice", "value": "100"})
    db.add(new_entry)
    db.commit()
    
    assert db.query(DynamicData).count() == 1
