import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    data = load_data("D:/ML/data/customer_churn.csv")
    print(data.head())