# Kidney Disease Classification with MLflow & DVC

A comprehensive MLOps project for kidney disease classification using Convolutional Neural Networks (CNN) with MLflow for experiment tracking and DVC for data version control.

## 🚀 Project Overview

This project implements an end-to-end machine learning pipeline for kidney disease classification using medical imaging. The project follows MLOps best practices with proper experiment tracking, model versioning, and deployment capabilities.

## 🛠️ Technologies Used

- **Deep Learning**: TensorFlow/Keras CNN
- **MLOps**: MLflow for experiment tracking
- **Data Version Control**: DVC
- **Web Framework**: Flask
- **Environment Management**: Conda
- **Version Control**: Git

## 📋 Project Workflows

The project follows a systematic workflow for development and deployment:

1. **Configuration Setup**
   - Update `config.yaml`
   - Update `secrets.yaml` [Optional]
   - Update `params.yaml`

2. **Code Development**
   - Update the entity definitions
   - Update the configuration manager in `src/config`
   - Update the components
   - Update the pipeline
   - Update `main.py`
   - Update `dvc.yaml`
   - Update `app.py`

## 🏗️ Project Structure

```
├── config/
│   └── config.yaml
├── src/
│   └── cnnClassifier/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
├── templates/
│   └── index.html
├── research/
│   └── trials.ipynb
├── params.yaml
├── requirements.txt
├── setup.py
├── template.py
├── README.md
└── app.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Conda (recommended)
- Git

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kallappa2005/MLOPS_KIDNEY_DISEASE_CNN
   cd MLOPS_KIDNEY_DISEASE_CNN
   ```

2. **Create and activate conda environment**
   ```bash
   conda create -n kidneycncnenv python=3.10 -y
   conda activate kidneycncnenv
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your web browser
   - Navigate to the localhost URL displayed in the terminal
   - The application will be running on the specified port

## 🔧 Configuration

The project uses several configuration files:

- **`config.yaml`**: Main configuration settings
- **`params.yaml`**: Model hyperparameters and training parameters
- **`secrets.yaml`**: API keys and sensitive information (optional)

## 📊 Model Training Pipeline

The training pipeline includes:

1. **Data Ingestion**: Loading and preprocessing medical images
2. **Data Validation**: Ensuring data quality and consistency
3. **Model Training**: CNN architecture training with MLflow tracking
4. **Model Evaluation**: Performance metrics and validation
5. **Model Deployment**: Serving the trained model via Flask API

## 🧪 Experiment Tracking

This project uses MLflow for comprehensive experiment tracking:

- Model parameters and hyperparameters
- Training metrics and validation scores
- Model artifacts and versioning
- Comparison of different model runs

## 📈 Data Version Control

DVC is integrated for:

- Data pipeline versioning
- Large file tracking
- Reproducible data processing
- Collaboration on datasets

## 🌐 Web Interface

The Flask application provides:

- User-friendly web interface
- Image upload functionality
- Real-time prediction results
- Model confidence scores

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Kallappa Kabbur**
- GitHub: [@Kallappa2005](https://github.com/Kallappa2005)
- Email: kallappakabbur874@gmail.com

## 🙏 Acknowledgments

- Thanks to the open-source community for the amazing tools
- Medical imaging datasets used for training
- MLflow and DVC communities for excellent documentation