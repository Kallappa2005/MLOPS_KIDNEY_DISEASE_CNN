# Kidney Disease Classification - End-to-End MLOps Project

## Live Demo

https://mlops-kidney-disease-cnn.onrender.com

This application predicts whether an uploaded kidney CT scan image is Normal or Tumor.

## What We Built

This project is a full end-to-end MLOps implementation for kidney disease image classification, including:

- Data and pipeline versioning with DVC
- Experiment tracking with MLflow
- Deep learning training and inference using TensorFlow/Keras
- Flask web application for real-time predictions
- Dockerized application for consistent local container runs
- Python-based testing for CI validation
- GitHub Actions CI/CD pipeline
- Production deployment on Render using Deploy Hook

## Model and Results

- Model type: CNN with transfer learning (VGG16 base)
- Input image size: 224 x 224
- Classes: Normal, Tumor
- Latest tracked metrics:
    - Accuracy: 0.8561
    - Loss: 0.2790

## Core Tech Stack

- Python 3.10
- TensorFlow / Keras
- Flask
- DVC
- MLflow
- Docker
- GitHub Actions
- Render

## Project Architecture

The workflow is organized into clear training and serving stages:

1. Data Ingestion
2. Base Model Preparation
3. Model Training
4. Model Evaluation
5. Prediction Serving via Flask API and UI

Main implementation areas:

- src/cnnClassifier/components for training pipeline components
- src/cnnClassifier/pipeline for stage orchestration and prediction pipeline
- config/config.yaml for project-level paths and runtime settings
- params.yaml for model and training parameters
- app.py for web routes and inference endpoint
- templates/index.html for frontend UI

## Local Development Setup

### Prerequisites

- Python 3.10
- Conda (recommended)
- Git

### Clone and Install

```bash
git clone https://github.com/Kallappa2005/MLOPS_KIDNEY_DISEASE_CNN
cd MLOPS_KIDNEY_DISEASE_CNN

conda create -n kidneyCnnenv python=3.10 -y
conda activate kidneyCnnenv

pip install -r requirements.txt
```

### Run Training Pipeline

```bash
python main.py
```

### Run Web Application

```bash
python app.py
```

Open the local URL shown in terminal and upload an image for prediction.

## DVC Usage

DVC is used to version data and pipeline outputs, making experiments reproducible.

Useful commands:

```bash
dvc init
dvc repro
dvc dag
dvc status
dvc metrics show
dvc add <path>
dvc push
dvc pull
dvc checkout
```

## MLflow Tracking

MLflow is used to log experiments, metrics, and model performance over runs.

Run MLflow UI locally:

```bash
mlflow ui
```

Optional DagsHub integration example:

```python
import dagshub

dagshub.init(
        repo_owner="kallappakabbur874",
        repo_name="MLOPS_KIDNEY_DISEASE_CNN",
        mlflow=True
)
```

## Docker Setup

This project includes a Dockerfile for containerized runs.

Build image:

```bash
docker build -t kidney-cnn:local .
```

Run container:

```bash
docker run -d --name kidney-cnn -p 8080:8080 kidney-cnn:local
```

Stop and remove:

```bash
docker stop kidney-cnn
docker rm kidney-cnn
```

## Python Testing

CI currently runs smoke tests from tests/test_ci_smoke.py.

Run tests locally:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## GitHub CI/CD

Workflow file:

- .github/workflows/ci-cd.yml

Current pipeline behavior:

1. Trigger on push to main and pull request to main
2. Setup Python and install requirements
3. Run Python tests
4. If event is push to main and tests pass, call Render Deploy Hook

Required GitHub secret:

- RENDER_DEPLOY_HOOK

## Render Deployment (Deploy Hook Based)

Deployment strategy used in this project:

- Render source-based web service
- GitHub Actions triggers Render deployment using Deploy Hook after tests pass

Render setup steps:

1. Create a new Render Web Service
2. Connect this GitHub repository
3. Set branch to main
4. Configure start command as python app.py (or gunicorn app:app if configured)
5. Ensure app binds to 0.0.0.0 and uses PORT
6. Copy Deploy Hook URL from Render service settings
7. Add the URL to GitHub secrets as RENDER_DEPLOY_HOOK

After this setup:

- Every push to main runs tests first
- If tests pass, CI triggers Render deploy hook
- Updated code is deployed to the live application

## Project Structure

High-level folders and files:

- src for ML components, configs, entities, pipelines, and utilities
- config for central YAML configuration
- artifacts for generated datasets and models
- model for deployable model artifacts
- templates for frontend HTML
- tests for CI test cases
- app.py for Flask app and endpoints
- main.py for training pipeline execution

## Future Improvements

- Add unit tests for each pipeline component
- Add integration tests for predict endpoint
- Add model confidence score in UI response
- Add model registry and version promotion flow
- Add environment-specific deployment workflows