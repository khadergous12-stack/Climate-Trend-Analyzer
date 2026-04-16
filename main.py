import os
import pandas as pd

from src.preprocessing import clean_data
from src.eda import perform_eda, heatmap_plot
from src.trend import trend_analysis, yearly_change_plot
from src.anomaly import detect_anomalies

# Create folders
os.makedirs("outputs/graphs", exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)

print("Loading dataset...")
df = pd.read_csv("data/GlobalLandTemperaturesByCity.csv")

print("Preprocessing...")
df = clean_data(df)

print("EDA...")
perform_eda(df)

print("Trend Analysis...")
trend_analysis(df)

print("Yearly Change...")
yearly_change_plot(df)

print("Heatmap...")
heatmap_plot(df)

print("Anomaly Detection...")
detect_anomalies(df)

print("\n✅ Done! Check outputs folder.")