import joblib
import pandas as pd


# Load saved model
model = joblib.load("D:/ML/model.pkl")


# Sample input data
sample_data = pd.DataFrame({

    "CustomerID": [2001],
    "Age": [40],
    "Gender": [1],
    "MonthlyCharges": [4500],
    "Tenure": [24]

})


# Predict
prediction = model.predict(sample_data)


print("Prediction:")
print(prediction)