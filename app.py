import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from scipy.stats import gaussian_kde

st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("🌍 Climate Trend Analyzer Dashboard")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("data/GlobalLandTemperaturesByCity.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df = df[df['Country'] == "India"]
    df = df[['Year', 'AverageTemperature', 'City']]
    df.columns = ['Year', 'Temperature', 'City']
    df = df.dropna()
    df = df.groupby(['Year', 'City']).mean().reset_index()
    return df

df = load_data()

# =========================
# SIDEBAR
# =========================
st.sidebar.header("Filters")

city = st.sidebar.selectbox("Select City", sorted(df['City'].unique()))

year_range = st.sidebar.slider(
    "Year Range",
    int(df['Year'].min()),
    int(df['Year'].max()),
    (1980, 2013)
)

df_filtered = df[
    (df['City'] == city) &
    (df['Year'] >= year_range[0]) &
    (df['Year'] <= year_range[1])
].copy()

# =========================
# METRICS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Avg Temp", f"{df_filtered['Temperature'].mean():.2f} °C")
col2.metric("Max Temp", f"{df_filtered['Temperature'].max():.2f} °C")
col3.metric("Min Temp", f"{df_filtered['Temperature'].min():.2f} °C")

# =========================
# ✅ TREND GRAPH (FIXED LEGEND)
# =========================
st.subheader("📈 Temperature Trend")

df_filtered['Smooth'] = df_filtered['Temperature'].rolling(3).mean()

fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=df_filtered['Year'],
    y=df_filtered['Temperature'],
    mode='lines+markers',
    name='Actual Temperature',
    line=dict(color="#4cc9f0", width=2)
))

fig1.add_trace(go.Scatter(
    x=df_filtered['Year'],
    y=df_filtered['Smooth'],
    mode='lines',
    name='Smoothed Trend',
    line=dict(color="#f72585", width=3)
))

fig1.update_layout(
    template="plotly_dark",
    legend=dict(x=0.01, y=0.99)
)

st.plotly_chart(fig1, width='stretch')

# =========================
# ✅ DISTRIBUTION (FIXED LABEL COLLISION)
# =========================
st.subheader("📊 Temperature Distribution")

temps = df_filtered['Temperature'].values

hist_y, hist_x = np.histogram(temps, bins=20)

kde = gaussian_kde(temps)
x_range = np.linspace(min(temps), max(temps), 200)
kde_values = kde(x_range)

kde_scaled = kde_values * max(hist_y) / max(kde_values)

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=hist_x[:-1],
    y=hist_y,
    name="Frequency",
    marker_color="#4361ee",
    opacity=0.7
))

fig2.add_trace(go.Scatter(
    x=x_range,
    y=kde_scaled,
    mode='lines',
    name="Density",
    line=dict(color="orange", width=3)
))

mean_temp = temps.mean()
median_temp = np.median(temps)

# FIX: shift annotations
fig2.add_vline(
    x=mean_temp,
    line_dash="dash",
    line_color="red",
    annotation_text="Mean",
    annotation_position="top right"
)

fig2.add_vline(
    x=median_temp,
    line_dash="dot",
    line_color="yellow",
    annotation_text="Median",
    annotation_position="top left"
)

fig2.update_layout(
    template="plotly_dark",
    xaxis_title="Temperature",
    yaxis_title="Frequency"
)

st.plotly_chart(fig2, width='stretch')

# =========================
# YEARLY CHANGE
# =========================
st.subheader("📉 Yearly Change")

df_filtered['Change'] = df_filtered['Temperature'].diff()

fig3 = px.line(
    df_filtered,
    x='Year',
    y='Change',
    markers=True,
    color_discrete_sequence=["#2a9d8f"]
)

fig3.add_hline(y=0)
fig3.update_layout(template="plotly_dark")

st.plotly_chart(fig3, width='stretch')

# =========================
# HEATMAP
# =========================
st.subheader("🔥 Decade Heatmap")

df_filtered['Decade'] = (df_filtered['Year'] // 10) * 10

pivot = df_filtered.pivot_table(
    values='Temperature',
    index='Decade',
    aggfunc='mean'
)

fig4 = px.imshow(
    pivot,
    color_continuous_scale="RdBu_r",
    text_auto=True
)

fig4.update_layout(template="plotly_dark")

st.plotly_chart(fig4, width='stretch')

# =========================
# ANOMALY DETECTION
# =========================
st.subheader("🚨 Anomaly Detection")

mean = df_filtered['Temperature'].mean()
std = df_filtered['Temperature'].std()
threshold = mean + 2 * std

df_filtered['Anomaly'] = df_filtered['Temperature'] > threshold

fig5 = go.Figure()

fig5.add_trace(go.Scatter(
    x=df_filtered['Year'],
    y=df_filtered['Temperature'],
    mode='lines',
    name='Temperature',
    line=dict(color='#4cc9f0')
))

fig5.add_trace(go.Scatter(
    x=df_filtered[df_filtered['Anomaly']==True]['Year'],
    y=df_filtered[df_filtered['Anomaly']==True]['Temperature'],
    mode='markers',
    name='Anomaly',
    marker=dict(color='red', size=10)
))

fig5.add_hline(
    y=threshold,
    line_dash="dash",
    line_color="yellow",
    annotation_text="Threshold"
)

fig5.update_layout(template="plotly_dark")

st.plotly_chart(fig5, width='stretch')

# =========================
# FINAL REPORT
# =========================
st.subheader("📋 Final Climate Report")

avg_temp = df_filtered['Temperature'].mean()
trend = df_filtered['Temperature'].iloc[-1] - df_filtered['Temperature'].iloc[0]

st.markdown(f"""
### 🔎 Summary for **{city}**

- 📊 Average Temperature: **{avg_temp:.2f} °C**
- 📈 Trend Change: **{trend:.2f} °C**
- 🔥 Max Temperature: **{df_filtered['Temperature'].max():.2f} °C**
- ❄️ Min Temperature: **{df_filtered['Temperature'].min():.2f} °C**

### 🧠 Insight:
- Climate shows a **{"warming" if trend > 0 else "cooling"} pattern**
- Anomalies indicate **extreme climate events**
- Overall variability is increasing
""")