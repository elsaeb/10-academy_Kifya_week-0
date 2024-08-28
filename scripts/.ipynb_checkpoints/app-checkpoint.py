import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data for each country
sierraleone_data = pd.read_csv('../data/sierraleone-bumbuna.csv')
benin_data = pd.read_csv('../data/benin-malanville.csv')
togo_data = pd.read_csv('../data/togo-dapaong_qc.csv')

# Combine data for comparison
benin_data['Country'] = 'Benin'
togo_data['Country'] = 'Togo'
sierraleone_data['Country'] = 'Sierra Leone'

combined_data = pd.concat([benin_data, togo_data, sierraleone_data])

# Convert timestamp to datetime
combined_data['Timestamp'] = pd.to_datetime(combined_data['Timestamp'])

st.header("Summary Statistics")
st.write(combined_data.groupby('Country').describe())

st.header("Data Quality Check")
st.write(combined_data.isnull().sum())

# For outliers, you can visualize with boxplots
st.header("Outliers Detection")
for col in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']:
    st.subheader(f'{col} Boxplot')
    fig, ax = plt.subplots()
    sns.boxplot(data=combined_data, x='Country', y=col, ax=ax)
    st.pyplot(fig)

st.header("Time Series Analysis")
for country in combined_data['Country'].unique():
    st.subheader(f'Time Series for {country}')
    country_data = combined_data[combined_data['Country'] == country]
    country_data = country_data.sort_values('Timestamp')
    st.line_chart(country_data.set_index('Timestamp')[['GHI', 'DNI', 'DHI', 'Tamb']])



st.header("Correlation Analysis")
for country in combined_data['Country'].unique():
    st.subheader(f'Correlation Matrix for {country}')
    country_data = combined_data[combined_data['Country'] == country]
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(country_data.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

import numpy as np

st.header("Wind Analysis")
for country in combined_data['Country'].unique():
    st.subheader(f'Wind Rose for {country}')
    country_data = combined_data[combined_data['Country'] == country]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax.scatter(np.radians(country_data['WD']), country_data['WS'], c=country_data['WSgust'], cmap='viridis')
    st.pyplot(fig)

# Temperature vs Solar Radiation
st.header("Temperature vs Solar Radiation")
for country in combined_data['Country'].unique():
    st.subheader(f'Temperature vs Solar Radiation for {country}')
    st.scatter_chart(country_data[['Tamb', 'GHI', 'DNI', 'DHI']])


st.header("Conclusion and Recommendations")

# Basic criteria based on GHI and DNI
suitability = combined_data.groupby('Country').agg({
    'GHI': 'mean',
    'DNI': 'mean',
    'Tamb': ['mean', 'std'],
    'RH': 'mean'
})

st.write(suitability)
