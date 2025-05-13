# Dev API - RapidAPI Integration

This README provides instructions on how to use the generated OpenAPI YAML file with RapidAPI and how to run the API locally for testing.

## Files Created

- `openapi.yaml`: The OpenAPI specification file that can be used with RapidAPI
- `generate_openapi.py`: Script to generate the OpenAPI YAML file
- `run_api.py`: Script to run the API locally for testing

## Running the API Locally

To run the API locally for testing:

```bash
python3 run_api.py
```

This will start the API server on http://localhost:8000. You can access:
- API documentation: http://localhost:8000/docs
- OpenAPI JSON schema: http://localhost:8000/openapi.json

## Using with RapidAPI

To use the generated OpenAPI YAML file with RapidAPI:

1. Log in to your RapidAPI account
2. Go to the "Add New API" section
3. Select "Import from OpenAPI/Swagger"
4. Upload the `openapi.yaml` file
5. Follow the RapidAPI prompts to complete the setup

## Regenerating the OpenAPI YAML File

If you make changes to the API (add new endpoints, modify existing ones), you can regenerate the OpenAPI YAML file by running:

```bash
python3 generate_openapi.py
```

## API Endpoints

The API currently has the following endpoints:

- `GET /developer`: Returns developer information
- `GET /health`: Returns health check status
- `GET /`: Returns a simple hello message

## Adding New Endpoints

To add new endpoints to the API:

1. Edit the `app.py` file to add new routes
2. Create Pydantic models for request/response schemas
3. Regenerate the OpenAPI YAML file using `generate_openapi.py`
4. Update your RapidAPI configuration with the new YAML file

## Dependencies

The project uses the following dependencies:
- FastAPI
- Uvicorn
- PyYAML
- Python-dotenv

These are listed in the `requirements.txt` file and can be installed with:

```bash
pip install -r requirements.txt