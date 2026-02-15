FROM python:3.11

# Carpeta donde se ejecutará el código dentro del contenedor
WORKDIR /app

# Copia dependencias e instalarlas
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia TODO el código del servicio FastAPI
COPY . .

# Comando para ejecutar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
