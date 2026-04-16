import pandas as pd

def clean_data(df):
    print("Cleaning dataset...")

    # Rename columns
    df = df.rename(columns={
        'dt': 'Date',
        'AverageTemperature': 'Temperature'
    })

    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter India (you can change to city if needed)
    df = df[df['Country'] == 'India']

    # Drop missing values
    df = df.dropna(subset=['Temperature'])

    # Extract Year
    df['Year'] = df['Date'].dt.year

    # Remove very old noisy data
    df = df[df['Year'] > 1900]

    # Group by Year
    df = df.groupby('Year')['Temperature'].mean().reset_index()

    print("Preprocessing completed!")

    return df