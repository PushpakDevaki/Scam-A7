import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Function to fetch COVID-19 data
@st.cache
def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Function to process data
def process_data(data):
    df = pd.DataFrame(data['Countries'])
    df = df[['Country', 'TotalConfirmed', 'TotalDeaths', 'TotalRecovered']]
    return df

# App title
st.title('COVID-19 Tracker')

# Fetch data
data_url = "https://api.covid19api.com/summary"
data = fetch_data(data_url)
df = process_data(data)

# Display data
st.header('COVID-19 Data')
st.write(df)

# Visualizations
st.header('Visualizations')

# Total cases per country
st.subheader('Total Cases Per Country')
plt.figure(figsize=(10, 5))
plt.barh(df['Country'], df['TotalConfirmed'], color='blue')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.title('Total Cases Per Country')
st.pyplot(plt)

# Total deaths per country
st.subheader('Total Deaths Per Country')
plt.figure(figsize=(10, 5))
plt.barh(df['Country'], df['TotalDeaths'], color='red')
plt.xlabel('Total Deaths')
plt.ylabel('Country')
plt.title('Total Deaths Per Country')
st.pyplot(plt)

# Total recoveries per country
st.subheader('Total Recoveries Per Country')
plt.figure(figsize=(10, 5))
plt.barh(df['Country'], df['TotalRecovered'], color='green')
plt.xlabel('Total Recoveries')
plt.ylabel('Country')
plt.title('Total Recoveries Per Country')
st.pyplot(plt)
