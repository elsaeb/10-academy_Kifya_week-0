import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from scipy.stats import zscore

# Load data for each country
sierraleone_data = pd.read_csv('dataset/sierraleone-bumbuna.csv')
benin_data = pd.read_csv('dataset/benin-malanville.csv')
togo_data = pd.read_csv('dataset/togo-dapaong_qc.csv')

# Function to perform analysis
def analyze_data(data, country_name):
    print(f"Analyzing data for {country_name}")

    # Summary Statistics
    summary_stats = data.describe()
    print(f"Summary Statistics for {country_name}:\n", summary_stats)

    # Check for missing values
    missing_values = data.isnull().sum()
    print(f"Missing Values in {country_name}:\n", missing_values)

    # Check for outliers (e.g., in GHI, DNI, DHI)
    outliers = data[(data['GHI'] < 0) | (data['DNI'] < 0) | (data['DHI'] < 0)]
    print(f"Outliers in {country_name}:\n", outliers)

    # Convert Timestamp to datetime
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Time Series Analysis
    plt.figure(figsize=(12, 6))
    plt.plot(data['Timestamp'], data['GHI'], label='GHI')
    plt.plot(data['Timestamp'], data['DNI'], label='DNI')
    plt.plot(data['Timestamp'], data['DHI'], label='DHI')
    plt.plot(data['Timestamp'], data['Tamb'], label='Tamb')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(f'Time Series of GHI, DNI, DHI, Tamb for {country_name}')
    plt.legend()
    plt.show()

    # Correlation Heatmap
    corr = data.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(f'Correlation Heatmap for {country_name}')
    plt.show()

    # Polar Plot for Wind Speed and Direction
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(projection='polar')
    scatter = ax.scatter(data['WD'] * np.pi / 180, data['WS'], c=data['WSgust'], cmap=cm.viridis, alpha=0.75)
    plt.colorbar(scatter, label='Wind Gust Speed (m/s)')
    plt.title(f'Wind Speed and Direction for {country_name}')
    plt.show()

    # Scatter plot to explore the influence of RH on temperature
    plt.figure(figsize=(12, 6))
    plt.scatter(data['RH'], data['Tamb'], alpha=0.5)
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Impact of Relative Humidity on Temperature for {country_name}')
    plt.show()

    # Histograms for GHI, DNI, DHI, WS, and temperatures
    data[['GHI', 'DNI', 'DHI', 'WS', 'Tamb']].hist(figsize=(15, 10), bins=50)
    plt.suptitle(f'Histograms of GHI, DNI, DHI, WS, and Temperature for {country_name}')
    plt.show()

    # Z-Score Analysis
    data['GHI_zscore'] = zscore(data['GHI'])
    zscore_outliers = data[data['GHI_zscore'].abs() > 3]
    print(f"Z-Score Outliers in {country_name}:\n", zscore_outliers)

    # Bubble Chart for GHI vs. Tamb vs. WS, with RH as bubble size
    plt.figure(figsize=(12, 6))
    plt.scatter(data['GHI'], data['Tamb'], s=data['RH']*10, alpha=0.5, c=data['WS'], cmap='viridis')
    plt.colorbar(label='Wind Speed (m/s)')
    plt.xlabel('GHI (W/m²)')
    plt.ylabel('Ambient Temperature (°C)')
    plt.title(f'Bubble Chart: GHI vs. Tamb vs. WS for {country_name} (Bubble Size: RH)')
    plt.show()

    return summary_stats, data

# Analyze each country
sierraleone_stats, sierraleone_cleaned = analyze_data(sierraleone_data, "Sierra Leone")
benin_stats, benin_cleaned = analyze_data(benin_data, "Benin")
togo_stats, togo_cleaned = analyze_data(togo_data, "Togo")

# Comparison Logic: Decide the best country based on GHI, DNI, and Tamb
def compare_countries(stats1, stats2, stats3):
    average_ghi = {'Sierra Leone': stats1['GHI']['mean'], 'Benin': stats2['GHI']['mean'], 'Togo': stats3['GHI']['mean']}
    average_dni = {'Sierra Leone': stats1['DNI']['mean'], 'Benin': stats2['DNI']['mean'], 'Togo': stats3['DNI']['mean']}
    average_tamb = {'Sierra Leone': stats1['Tamb']['mean'], 'Benin': stats2['Tamb']['mean'], 'Togo': stats3['Tamb']['mean']}
    
    # Compare GHI and DNI, higher is better; for Tamb, lower is generally better.
    best_country = max(average_ghi, key=average_ghi.get)  # Just an example using GHI
    
    print(f"Best country based on GHI: {best_country}")
    return best_country

best_country = compare_countries(sierraleone_stats, benin_stats, togo_stats)

# Streamlit code to integrate this into an interactive app
import streamlit as st

st.title("Solar Investment Recommendation")

st.write(f"Based on the analysis, {best_country} is recommended as the most suitable country for solar investment.")