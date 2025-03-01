# Usa una imagen base de Python
FROM python:3.9

# Define el directorio de trabajo dentro del contenedor
WORKDIR /Monitoring-and-Data-Processing-Platform

# Copia los archivos de dependencias y los instala
COPY api/libraries.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código dentro del contenedor
COPY . .

# Expone el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para ejecutar la API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
