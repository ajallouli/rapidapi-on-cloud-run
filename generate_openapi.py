import yaml
import json
from app import app

# Get the OpenAPI schema from FastAPI
openapi_schema = app.openapi()

# Convert to YAML
yaml_content = yaml.dump(openapi_schema, sort_keys=False)

# Write to file
with open("openapi.yaml", "w") as f:
    f.write(yaml_content)

print("OpenAPI YAML file generated successfully at openapi.yaml")