import pandas as pd

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset


# Training Dataset
reference_data = pd.read_csv("data/customer_churn.csv")


# Production Dataset
current_data = pd.read_csv("data/customer_churn.csv")


# Artificial Drift
current_data["Age"] = current_data["Age"] + 20


# Create Drift Report
report = Report(metrics=[
    DataDriftPreset()
])


# Run Report
report.run(
    reference_data=reference_data,
    current_data=current_data
)


# Save HTML Report
report.save_html("drift_report.html")


print("Drift report generated successfully!")