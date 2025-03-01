from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    column1 = Column(String)
    column2 = Column(Float)
    # Add more columns as needed