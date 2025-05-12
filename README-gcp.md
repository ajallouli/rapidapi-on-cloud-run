# Setting on GCP
## Login to GCP
```sh
gcloud auth login
```

## Enabling APIs for Cloud Run

```sh
# Needed APIs for GCP Cloud Run
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
```

## Defining the cloudbuild.yml
Refer the link https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run for more details.
```yml
steps:
# Build the image
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'us-central1-docker.pkg.dev/rapidai-project/dev-api/dev-api-image', '.']
# Push the image to Artifact Registry
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'us-central1-docker.pkg.dev/rapidai-project/dev-api/dev-api-image']
# Deploy image to Cloud Run
- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
  entrypoint: gcloud
  args: ['run', 'deploy', 'dev-api-service', '--image', 'us-central1-docker.pkg.dev/rapidai-project/dev-api/dev-api-image', '--region', 'us-central1']
images:
- 'us-central1-docker.pkg.dev/rapidai-project/dev-api/dev-api-image'
```

## Ensure the Artifact Registry repository exists:
```sh
gcloud artifacts repositories create dev-api \
  --repository-format=docker \
  --location=us-central1 \
  --description="Repository for dev-api images"
```
## Grant proper IAM permissions to your service account
```sh
gcloud projects add-iam-policy-binding rapidai-project \
  --member="serviceAccount:946651860821-compute@developer.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"
```

## Check Docker Authentication:
Configure Docker to authenticate with Artifact Registry

```sh
gcloud auth configure-docker us-central1-docker.pkg.dev
```

## submit
```sh
# define project id
export PROJECT_ID=rapidai-project
echo $PROJECT_ID

# define project number
export PROJECT_NUMBER=$(gcloud projects list --format="value(project_number)" --filter="projectId=$PROJECT_ID")
echo $PROJECT_NUMBER

## binding roles to the service account
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/logging.logWriter"

```

```sh
gcloud builds submit --region=us-central1
```