FROM python:3.9

WORKDIR /Monitoring-and-Data-Processing-Platform

COPY api/libraries.txt .

RUN pip install --no-cache-dir -r libraries.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
