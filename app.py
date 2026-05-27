from fastapi import FastAPI
import joblib
import pandas as pd

from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

# Load ML model
model = joblib.load("model.pkl")


@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API Running"
    }


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return {
        "prediction": int(prediction[0])
    }


# Prometheus Metrics
Instrumentator().instrument(app).expose(app)