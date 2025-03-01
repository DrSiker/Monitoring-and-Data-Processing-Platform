from fastapi import FastAPI
from routes import router

app = FastAPI(title="Plataforma de Monitoreo CSV Dinámico")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API en ejecución 🚀"}

