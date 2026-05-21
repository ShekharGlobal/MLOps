# MLOps Project - Customer Churn Prediction

## Project Overview

This project demonstrates an end-to-end MLOps pipeline using Python, FastAPI, Docker, and GitHub Actions.

The system predicts customer churn using a Machine Learning model and exposes predictions through REST APIs.

---

# Tech Stack

- Python
- Pandas
- Scikit-learn
- FastAPI
- Docker
- Docker Compose
- GitHub Actions
- GitHub

---

# Project Workflow

```text
Customer Dataset
        ↓
Data Ingestion
        ↓
Data Preprocessing
        ↓
Model Training
        ↓
Model Saving
        ↓
Prediction System
        ↓
FastAPI Deployment
        ↓
Docker Containerization
        ↓
CI/CD Pipeline
```

---

# Project Structure

```bash
ML/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── data/
│   └── customer_churn.csv
│
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── app.py
├── data_ingestion.py
├── preprocessing.py
├── model_training.py
├── predict.py
├── save_model.py
├── train.py
├── model.pkl
└── README.md
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/ShekharGlobal/MLOps.git
```

---

## Install Dependencies

```bash
pip install pandas
pip install scikit-learn
pip install fastapi
pip install uvicorn
pip install joblib
```

---

# Run Model Training

```bash
py model_training.py
```

---

# Run Prediction

```bash
py predict.py
```

---

# Run FastAPI Application

```bash
uvicorn app:app --reload
```

OR

```bash
py -m uvicorn app:app --reload
```

---

# Swagger API Documentation

Open browser:

```text
http://127.0.0.1:8000/docs
```

---

# Docker Commands

## Build Docker Image

```bash
docker build -t churn-api .
```

## Run Docker Container

```bash
docker run -p 8000:8000 churn-api
```

---

# Docker Compose

```bash
docker compose up
```

---

# CI/CD Pipeline

GitHub Actions workflow automatically:

- Installs dependencies
- Runs training script
- Builds Docker image

Workflow file:

```text
.github/workflows/main.yml
```

---

# Features

- Modular Python project structure
- ML model training pipeline
- REST API deployment
- Dockerized application
- GitHub Actions CI/CD
- End-to-end MLOps workflow

---

# Future Enhancements

- MLflow Integration
- Kubernetes Deployment
- Model Monitoring
- Cloud Deployment
- Automated Retraining

---

# Author

Shekhar