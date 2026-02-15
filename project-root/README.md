Candidate Intelligence System
FastAPI + Flask AI + Qdrant + ETL + Rust Worker + React + Svelte MF
🚀 Descripción del Proyecto

Este sistema es una plataforma inteligente diseñada para:

1. Registrar candidatos (CRUD completo)

2. Procesar hojas de vida en PDF

3. Extraer texto y transformarlo

4. Guardar candidatos en PostgreSQL

5. Generar embeddings con IA (Flask + SentenceTransformer)

6. Indexar en Qdrant para búsqueda semántica

7. Realizar análisis e insights usando modelos OpenAI

8. Ejecutar cargas masivas con un worker en Rust

9. Integrar microfrontends con Svelte

10. Mostrar todo en un frontend React moderno


ARQUITECTURA DEL PROYECTO 
project-root/
  docs/
  infra/
    .env
    docker-compose.yml
  pipelines/
    etl/
      venv/
      .env
      etl_runner.py
      extract.py
      transform.py
      load.py
      mass_runner.py
      requirements.txt
      pdfs/
  services/
    api_fastapi/
      app/
      migrations/
      .env
      alembic.ini
      Dockerfile
    api-flask/
      venv/
      app.py
      requirements.txt
    frontend-react/
    worker-rust/
      mass_pdf_worker/
        src/
        Dockerfile
  ui/
    svelte-mf/
      assets/
      lib/
      src/
      .env
  venv/


Tecnologías Utilizadas:

FastAPI → API principal, CRUD, insights.

Flask → microservicio de embeddings y búsquedas.

Qdrant → vector database para búsquedas semánticas.

PostgreSQL → base de datos relacional.

Rust → worker para cargas masivas de PDFs.

React + Vite → frontend principal.

Svelte → microfrontend.

Docker Compose → orquestación de todos los servicios.

OpenAI → generación de insights avanzados.

ETL Pipeline → extracción, transformación y carga desde PDFs.


LEVANTAR TODA LA ARQUITECTURA COMPLETA: 

Desde project-root/infra/ ejecuta: 
docker compose up --build
levanta:

| Servicio         | URL                                                                |
| ---------------- | ------------------------------------------------------------------ |
| FastAPI          | [http://localhost:8000](http://localhost:8000)                     |
| Flask AI         | [http://localhost:5001](http://localhost:5001)                     |
| Qdrant Dashboard | [http://localhost:6333/dashboard](http://localhost:6333/dashboard) |
| React App        | [http://localhost:5173](http://localhost:5173)                     |
| Svelte MF        | [http://localhost:5174](http://localhost:5174)                     |




Búsqueda Semántica: 

POST http://localhost:8000/search/semantic-search
{
  "query": "python backend senior"
}

Insights con OpenAI: 
POST http://localhost:8000/insights
{
  "candidate_id": 5,
  "job_description": "Buscamos developer con experiencia en FastAPI y PostgreSQL"
}



Frontend React: 
cd services/frontend-react
npm install
npm run dev



Microfrontend svelte: 
cd ui/svelte-mf
npm install
npm run dev
