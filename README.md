# Kidney Disease Classification - MLflow DVC

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

### Dvc Commands 
1. dvc init
2. dvc repro
3. dvc dag