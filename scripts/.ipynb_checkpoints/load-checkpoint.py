import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data for each country
sierraleone_data = pd.read_csv('../data/sierraleone-bumbuna.csv')
benin_data = pd.read_csv('../data/benin-malanville.csv')
togo_data = pd.read_csv('../data/togo-dapaong_qc.csv')

# Function to plot data
def plot_data(data, title):
    fig, ax = plt.subplots()
    sns.lineplot(data=data[['GHI', 'DNI', 'DHI', 'Tamb']])
    ax.set_title(title)
    st.pyplot(fig)

# Create a sidebar for country selection
country = st.sidebar.selectbox('Select Country', ('Sierra Leone - Bimbuna', 'Benin - Malanville', 'Togo - Dapaong'))

# Show data and analysis based on selection
if country == 'Sierra Leone - Bimbuna':
    data = sierraleone_data
elif country == 'Benin - Malanville':
    data = benin_data
else:
    data = togo_data

# Display data
st.write(f"Data for {country}")
st.dataframe(data.head())

# Summary Statistics
st.write("Summary Statistics:")
st.write(data.describe())

# Plot data
st.write(f"Solar Radiation and Temperature for {country}")
plot_data(data, f"Solar Radiation and Temperature for {country}")

# Additional insights (add correlation analysis, etc.)
st.write("Correlation Matrix:")
st.write(data.corr(numeric_only=True))

