from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

from data_ingestion import load_data
from preprocessing import preprocess_data


# Load dataset
df = load_data("data/customer_churn.csv")


# Preprocess dataset
X_train, X_test, y_train, y_test = preprocess_data(df)


# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Predictions
predictions = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, predictions)


print("Predictions:")
print(predictions)

print("\nAccuracy:")
print(accuracy)


# Save model
joblib.dump(model, "model.pkl")

print("\nModel saved successfully!")
print("CI/CD Pipeline Triggered Successfully")