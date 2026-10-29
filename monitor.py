
from sklearn.datasets import load_iris
from evidently import Report
from evidently.presets import DataDriftPreset

iris = load_iris(as_frame=True)
data = iris.data

reference_data = data.iloc[:75].copy()
current_data = data.iloc[75:].copy()

report = Report([DataDriftPreset()])

snapshot = report.run(
    current_data=current_data,
    reference_data=reference_data,
)

snapshot.save_html("evidently_report.html")

print("Iris monitoring completed.")
print("Report saved to evidently_report.html")