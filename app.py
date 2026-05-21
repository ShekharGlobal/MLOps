from fastapi import FastAPI
import joblib
import pandas as pd


# Create FastAPI app
app = FastAPI()


# Load trained model
model = joblib.load("model.pkl")


@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API Running"
    }


@app.post("/predict")
def predict(data: dict):

    # Convert input to dataframe
    df = pd.DataFrame([data])

    # Prediction
    prediction = model.predict(df)

    return {
        "prediction": int(prediction[0])
    }