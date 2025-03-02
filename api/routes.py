from fastapi import APIRouter, UploadFile, File, Depends
import pandas as pd
from sqlalchemy.orm import Session
import io
import logging
from api.database import SessionLocal, engine, Base
from api.models import Metadata, DynamicData
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


router = APIRouter()

Base.metadata.create_all(bind=engine)

REQUEST_COUNT = Counter("http_requests_total", "Total de solicitudes HTTP", ["method", "endpoint"])
UPLOAD_SUCCESS = Counter("upload_csv_success_total", "Total de archivos CSV subidos con éxito")
UPLOAD_FAILURE = Counter("upload_csv_failure_total", "Total de errores en carga de archivos CSV")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Leer CSV sin nombres de columnas fijos
        df = pd.read_csv(io.StringIO(file.file.read().decode("utf-8")))
        
        # Guardar el esquema del CSV en la tabla metadata
        schema = {col: str(df[col].dtype) for col in df.columns}
        metadata_entry = Metadata(filename=file.filename, schema=schema)
        db.add(metadata_entry)
        
        # Guardar los datos como JSON en la tabla DynamicData
        for _, row in df.iterrows():
            new_entry = DynamicData(data=row.to_dict())
            db.add(new_entry)
        
        db.commit()
        return {"message": f"Archivo {file.filename} procesado y almacenado"}
    except Exception as e:
        logger.error(f"Error al procesar archivo: {str(e)}")
        return {"error": "No se pudo procesar el archivo"}

@router.get("/data")
def get_data(db: Session = Depends(get_db)):
    data = db.query(DynamicData).all()
    return [entry.data for entry in data]

@router.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)