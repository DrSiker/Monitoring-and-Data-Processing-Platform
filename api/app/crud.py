from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    import csv
    contents = await file.read()
    decoded = contents.decode("utf-8")
    reader = csv.DictReader(decoded.splitlines())
    for row in reader:
        data = schemas.DataCreate(**row)
        crud.create_data(db, data)
    return {"message": "File uploaded successfully"}

@router.get("/data")
def get_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_data(db, skip=skip, limit=limit)
    return data