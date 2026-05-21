import joblib

from sklearn.ensemble import RandomForestClassifier

from data_ingestion import load_data
from preprocessing import preprocess_data


# Load data
df = load_data("D:/ML/data/customer_churn.csv")

# Preprocess data
X_train, X_test, y_train, y_test = preprocess_data(df)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "D:/ML/model.pkl")

print("Model saved successfully!")