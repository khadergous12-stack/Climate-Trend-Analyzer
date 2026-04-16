import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# TREND GRAPH (MAIN)
# =========================
def trend_analysis(df):
    print("Generating trend graph...")

    sns.set_theme(style="white")

    df_recent = df.tail(50).copy()
    df_recent['Rolling'] = df_recent['Temperature'].rolling(5).mean()

    plt.figure(figsize=(12,6), dpi=120)

    plt.plot(df_recent['Year'], df_recent['Temperature'],
             color="#457b9d", linewidth=2, marker='o', markersize=3, label="Actual")

    plt.plot(df_recent['Year'], df_recent['Rolling'],
             color="#e63946", linewidth=3, label="Trend")

    plt.title("Temperature Trend (Last 50 Years)", fontsize=16, fontweight='bold')
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")

    plt.legend()
    plt.grid(alpha=0.2)

    plt.tight_layout()
    plt.savefig("outputs/graphs/trend.png", dpi=300)
    plt.close()


# =========================
# NEW GRAPH (IMPORTANT 🔥)
# =========================
def yearly_change_plot(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    print("Generating improved yearly change graph...")

    sns.set_theme(style="white")

    df_recent = df.tail(50).copy()
    df_recent['Change'] = df_recent['Temperature'].diff()

    plt.figure(figsize=(12,6), dpi=120)

    # Line
    plt.plot(df_recent['Year'], df_recent['Change'],
             color="#2a9d8f", linewidth=2, marker='o', markersize=4,
             label="Yearly Change")

    # Positive area
    plt.fill_between(df_recent['Year'], df_recent['Change'], 0,
                     where=(df_recent['Change'] >= 0),
                     alpha=0.3,
                     label="Increase")

    # Negative area
    plt.fill_between(df_recent['Year'], df_recent['Change'], 0,
                     where=(df_recent['Change'] < 0),
                     alpha=0.3,
                     label="Decrease")

    # Zero line
    plt.axhline(0, color='black', linewidth=1, label="No Change")

    plt.title("Year-to-Year Temperature Change", fontsize=16, fontweight='bold')
    plt.xlabel("Year")
    plt.ylabel("Change (°C)")

    plt.legend()   # 🔥 THIS FIXES YOUR ISSUE

    plt.grid(alpha=0.2)

    plt.tight_layout()
    plt.savefig("outputs/graphs/yearly_change.png", dpi=300)
    plt.close()