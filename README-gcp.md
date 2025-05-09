# Setting on GCP
## Login to GCP
```sh
gcloud auth login
```

## Enabling APIs for Cloud Run

```sh
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
```
