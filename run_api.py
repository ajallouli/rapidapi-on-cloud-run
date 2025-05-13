import uvicorn

if __name__ == "__main__":
    print("Starting Dev API server...")
    print("API documentation available at: http://localhost:8000/docs")
    print("OpenAPI schema available at: http://localhost:8000/openapi.json")
    print("Press CTRL+C to stop the server")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)