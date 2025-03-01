from sqlalchemy.orm import Session
from . import models, schemas

def create_data(db: Session, data: schemas.DataCreate):
    db_data = models.Data(**data.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Data).offset(skip).limit(limit).all()