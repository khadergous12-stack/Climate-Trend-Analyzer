import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# EDA FUNCTION
# =========================
def perform_eda(df):
    print("Generating EDA graphs...")

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(10,5), dpi=120)
    sns.histplot(df['Temperature'], kde=True, color="#2a9d8f", bins=25)

    plt.title("Temperature Distribution (India)", fontsize=14, fontweight='bold')
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("outputs/graphs/histogram.png", dpi=300)
    plt.close()

    print("EDA done!")


# =========================
# HEATMAP
# =========================
def heatmap_plot(df):
    print("Generating heatmap...")

    sns.set_theme(style="white")

    df = df.copy()
    df['Decade'] = (df['Year'] // 10) * 10

    pivot = df.pivot_table(
        values='Temperature',
        index='Decade',
        aggfunc='mean'
    )

    plt.figure(figsize=(6,6), dpi=120)

    sns.heatmap(
        pivot,
        cmap="coolwarm",
        annot=True,
        fmt=".2f",
        linewidths=0.5,
        cbar_kws={'label': 'Temperature (°C)'}
    )

    plt.title("Decade-wise Temperature Heatmap", fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig("outputs/graphs/heatmap.png", dpi=300)
    plt.close()