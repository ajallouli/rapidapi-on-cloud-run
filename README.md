# Developer API

A production-ready Python REST API using Flask and Gunicorn.

## Features

- Flask web framework
- Gunicorn WSGI server with gevent workers
- Single endpoint `/developper` that returns `{'dev': 'amine'}`
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

3. Or run with Gunicorn:
   ```
   gunicorn --bind 0.0.0.0:8000 --workers=2 --worker-class=gevent app:app
   ```

### Using Docker Compose

1. Build and start the container:
   ```
   docker-compose up --build
   ```

2. Access the API at http://localhost:8000/developper

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

- `/developper` - Returns `{'dev': 'amine'}`
- `/health` - Health check endpoint, returns `{'status': 'ok'}`

