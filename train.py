from data_ingestion import load_data
from preprocessing import preprocess_data


df = load_data("D:/ML/data/customer_churn.csv")

X_train, X_test, y_train, y_test = preprocess_data(df)

print("X Train")
print(X_train.head())

print("\nY Train")
print(y_train.head())