# Kidney Disease Classification - MLflow DVC
run mlflow ui

## Project Overview
This is a kidney disease classification project using deep learning with MLflow for experiment tracking and DVC for data version control.

## Development Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

## How to Run

### Prerequisites
Clone the repository:
```bash
https://github.com/Kallappa2005/MLOPS_KIDNEY_DISEASE_CNN
```

### Installation Steps

**STEP 01** - Create a conda environment after opening the repository:
```bash
conda create -n kidneyCnnenv python=3.10 -y
conda activate kidneyCnnenv
```

**STEP 02** - Install the requirements:
```bash
pip install -r requirements.txt
```

**STEP 03** - Run the application:
```bash
python main.py
```

Now, open up your local host and port to access the application.

## MLflow Setup

### Documentation
- [MLflow tutorial](https://mlflow.org/docs/latest/tutorials-and-examples/tutorial.html)

### Running MLflow UI
```bash
mlflow ui
```

```python
import dagshub

dagshub.init(
    repo_owner="kallappakabbur874",
    repo_name="MLOPS_KIDNEY_DISEASE_CNN",
    mlflow=True
)
```


### DVC Commands 
1. `dvc init` - Initialize DVC in your project.
2. `dvc repro` - Reproduce the entire pipeline or specific stages.
3. `dvc dag` - Visualize the pipeline as a directed acyclic graph.
4. `dvc status` - Check if data or pipeline has changed.
5. `dvc metrics show` - Display metrics from experiments and runs.
6. `dvc add` - Tell DVC to track a dataset or model file.
7. `dvc remote add` - Add a remote storage (cloud / DagsHub / local).
8. `dvc remote list` - Show all configured DVC remotes.
9. `dvc push` - Upload data/models to remote storage.
10. `dvc pull` - Download data/models from remote storage.
11. `dvc checkout` - Restore data to the version in .dvc files.

## GitHub CI/CD (Test -> Deploy to Render)

This project includes a GitHub Actions workflow at `.github/workflows/ci-cd.yml`.

### Pipeline Flow
1. Run smoke tests from `tests/test_ci_smoke.py`
2. Trigger a Render deploy hook
3. Render builds and deploys the latest `main` branch code

### Required GitHub Repository Secrets

Set these secrets in GitHub:

- `RENDER_DEPLOY_HOOK`

## Render Deployment

1. In Render, create a new Web Service.
2. Connect this GitHub repository.
3. Set the branch to `main`.
4. Use a Python source-based service, not a Docker image service.
5. Set the start command to `python app.py` or `gunicorn app:app` if you later add gunicorn.
6. Make sure the app binds to `0.0.0.0` and uses the `PORT` environment variable.
7. Open the service settings and copy the Deploy Hook URL.
8. Store that URL as the GitHub secret `RENDER_DEPLOY_HOOK`.

When code is pushed to `main`, GitHub Actions runs tests first. If tests pass, the workflow calls Render's deploy hook and Render rebuilds and redeploys the app from source.