from pydantic import BaseModel

class DataCreate(BaseModel):
    column1: str
    column2: float
    # Add more fields as needed

class Data(DataCreate):
    id: int

    class Config:
        orm_mode = True