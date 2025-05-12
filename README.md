# Developer API

A production-ready Python REST API using FastAPI and Uvicorn/Gunicorn.

## Features

- FastAPI web framework
- Uvicorn ASGI server with Gunicorn workers
- Automatic OpenAPI documentation
- Single endpoint `/developper` that returns `{"dev": "amine"}`
- Containerized with Docker
- Ready for deployment to Google Cloud Run

## Local Development

### Running directly

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the development server:
   ```
   python app.py
   ```

3. Or run with Uvicorn:
   ```
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

4. Or run with Gunicorn:
   ```
   gunicorn --bind 0.0.0.0:8000 --workers=2 --worker-class=uvicorn.workers.UvicornWorker app:app
   ```

### Using Docker Compose

1. Build and start the container:
   ```
   docker-compose up --build
   ```

2. Access the API at http://localhost:8000/developper
3. Access API documentation at http://localhost:8000/docs or http://localhost:8000/redoc

## Deployment to Google Cloud Run

```bash
# Build the container
docker build -t gcr.io/[PROJECT_ID]/dev-api .

# Push to Google Container Registry
docker push gcr.io/[PROJECT_ID]/dev-api

# Deploy to Cloud Run
gcloud run deploy dev-api \
  --image gcr.io/[PROJECT_ID]/dev-api \
  --platform managed \
  --allow-unauthenticated
```

## API Endpoints

- `/developper` - Returns `{"dev": "amine"}`
- `/health` - Health check endpoint, returns `{"status": "ok"}`
- `/docs` - Interactive API documentation (Swagger UI)
- `/redoc` - Alternative API documentation (ReDoc)

