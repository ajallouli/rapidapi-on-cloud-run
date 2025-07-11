import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Define response models
class DeveloperResponse(BaseModel):
    dev: str

class HealthResponse(BaseModel):
    status: str

class HomeResponse(BaseModel):
    hello: str

app = FastAPI(
    title="Dev API",
    description="A simple API for development",
    version="1.0.0"
)

@app.get('/developer', response_model=DeveloperResponse)
def get_developer():
    return {"dev": "amine"}

@app.get('/health', response_model=HealthResponse)
def health_check():
    return {"status": "ok"}

@app.get('/', response_model=HomeResponse)
def home():
    return {"hello": "ok"}

# This is only used when running the app directly with Python
# When using uvicorn or gunicorn, this block is not executed
if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get('PORT', 8000))  # PORT is now loaded from .env if available
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
