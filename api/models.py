from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Metadata(Base):
    __tablename__ = "metadata"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    schema = Column(JSON)  # Guardamos el esquema del CSV

class DynamicData(Base):
    __tablename__ = "dynamic_data"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)  # Datos en formato JSON flexible
