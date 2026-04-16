# 🌍 Climate Trend Analyzer Dashboard

An advanced interactive data analytics dashboard built using **Streamlit** to explore, analyze, and visualize historical climate data across Indian cities.

This project focuses on uncovering long-term temperature trends, identifying anomalies, and generating meaningful insights using real-world data.

---

## 📌 Project Overview

Climate change is one of the most pressing global challenges. Understanding historical temperature trends helps in identifying patterns, predicting future behavior, and making informed decisions.

This project uses historical land temperature data to:

- Analyze temperature variations over time  
- Detect unusual or extreme temperature events  
- Visualize climate behavior in an intuitive dashboard  
- Generate insights automatically  

---

## 🚀 Features

### 📈 Temperature Trend Analysis
- Visualizes yearly temperature changes
- Includes smoothed trend line for better interpretation
- Helps identify long-term warming or cooling patterns

---

### 📊 Temperature Distribution
- Histogram with smooth density curve (KDE)
- Displays mean and median clearly
- Provides insight into data spread and skewness

---

### 📉 Year-to-Year Temperature Change
- Shows fluctuations between consecutive years
- Helps identify unstable or volatile climate periods

---

### 🔥 Decade-wise Heatmap
- Aggregates temperature data into decades
- Highlights long-term climate changes visually

---

### 🚨 Anomaly Detection
- Identifies extreme temperature values
- Uses statistical threshold (mean + standard deviation)
- Clearly highlights anomalies on the graph

---

### 📋 Final Climate Report
- Automatically generated summary
- Includes:
  - Average temperature  
  - Overall trend change  
  - Maximum & minimum values  
- Provides key insights for quick understanding

---

## 🧠 Technologies Used

- **Python** – Core programming language  
- **Streamlit** – Interactive dashboard framework  
- **Plotly** – Advanced visualizations  
- **Pandas** – Data processing  
- **NumPy** – Numerical computations  
- **SciPy** – Statistical analysis (KDE)

---

## 📊 Dataset Information

- **Dataset Name:** Global Land Temperatures by City  
- **Source:** Berkeley Earth (Kaggle)  
- **Time Range:** 1743 – 2013  
- **Region Used:** India  

> ⚠️ Note: The dataset ends in 2013, so analysis is limited to historical data only.

---

## 📥 Dataset Download

Due to GitHub file size limitations, the dataset is not included in this repository.

Download it from:
👉 https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data

After downloading, place it in:


data/GlobalLandTemperaturesByCity.csv


---

## 🏗️ Project Structure


Climate-Trend-Analyzer/
│
├── app.py # Streamlit dashboard
├── requirements.txt # Dependencies
├── README.md # Documentation
│
├── data/
│ └── GlobalLandTemperaturesByCity.csv
│
├── outputs/
│ ├── graphs/
│ └── reports/
│
├── src/
│ ├── preprocessing.py
│ ├── eda.py
│ ├── trend.py
│ └── anomaly.py


---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/Climate-Trend-Analyzer.git

cd Climate-Trend-Analyzer


---

### 2️⃣ Install Dependencies

pip install -r requirements.txt


---

### 3️⃣ Run Dashboard

streamlit run app.py


---

## 📊 Key Insights

- Temperature trends show a gradual increase over time  
- Climate variability has increased in recent decades  
- Extreme temperature anomalies are more frequent in later years  
- Clear long-term warming pattern observed  

---

## 🎯 Learning Outcomes

- Real-world data analysis and preprocessing  
- Data visualization using Plotly  
- Statistical anomaly detection  
- Dashboard development using Streamlit  
- Converting raw data into actionable insights  

---

## 🔮 Future Enhancements

- Add real-time climate data integration  
- Deploy dashboard online  
- Add predictive modeling (ML-based forecasting)  
- Multi-country comparison  
- Export reports as PDF  

---

## 👨‍💻 Author

**Khader Gouse**

---

## ⭐ Support

If you found this project useful:
- ⭐ Star the repository  
- 🔗 Share it  
- 💬 Give feedback  

---

## 📬 Contact

Feel free to connect or reach out for collaboration opportunities.
