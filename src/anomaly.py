import matplotlib.pyplot as plt
import seaborn as sns

def detect_anomalies(df):
    print("Detecting anomalies with visualization...")

    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Anomaly'] = df['Temperature'].apply(
        lambda x: 1 if abs(x - mean) > 2 * std else 0
    )

    df.to_csv("outputs/reports/anomalies.csv", index=False)

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(12,6), dpi=120)

    # Normal data
    plt.plot(df['Year'], df['Temperature'],
             color="#1d3557", linewidth=1.5, label="Temperature")

    # Highlight anomalies
    plt.scatter(df[df['Anomaly'] == 1]['Year'],
                df[df['Anomaly'] == 1]['Temperature'],
                color="#e63946", s=60, label="Anomaly")

    plt.title("Climate Anomaly Detection", fontsize=16, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)

    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("outputs/graphs/anomalies.png", dpi=300)
    plt.close()

    print("Anomaly detection completed!")