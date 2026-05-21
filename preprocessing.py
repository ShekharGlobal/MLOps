from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):

    encoder = LabelEncoder()

    # Convert categorical columns
    df["Gender"] = encoder.fit_transform(df["Gender"])
    df["Churn"] = encoder.fit_transform(df["Churn"])

    # Features and target
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test