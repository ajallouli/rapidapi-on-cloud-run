import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Dev API",
    description="A simple API for development",
    version="1.0.0"
)

@app.get('/developper')
def get_developer():
    return {"dev": "amine"}

@app.get('/health')
def health_check():
    return {"status": "ok"}

@app.get('/')
def home():
    return {"hello": "ok"}

# This is only used when running the app directly with Python
# When using uvicorn or gunicorn, this block is not executed
if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get('PORT', 8000))  # PORT is now loaded from .env if available
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
