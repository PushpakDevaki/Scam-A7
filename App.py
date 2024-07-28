import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load and process data
@st.cache
def load_data(file):
    data = pd.read_csv(file)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

# Function to plot total streams over time
def plot_total_streams(data):
    total_streams = data.groupby('Date')['Streams'].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(total_streams.index, total_streams.values, marker='o')
    plt.title('Total Streams Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Streams')
    st.pyplot(plt)

# Function to plot average streams per song over time
def plot_avg_streams(data):
    avg_streams = data.groupby('Date')['Streams'].mean()
    plt.figure(figsize=(10, 5))
    plt.plot(avg_streams.index, avg_streams.values, marker='o', color='orange')
    plt.title('Average Streams Per Song Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Streams')
    st.pyplot(plt)

# Function to plot distribution of streams
def plot_stream_distribution(data):
    plt.figure(figsize=(10, 5))
    plt.hist(data['Streams'], bins=30, color='purple', edgecolor='black')
    plt.title('Distribution of Streams')
    plt.xlabel('Streams')
    plt.ylabel('Frequency')
    st.pyplot(plt)

# App title
st.title('Music Streaming Analysis Tool')

# File uploader
uploaded_file = st.file_uploader('Upload your CSV file', type=['csv'])

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write(data.head())

    st.header('Visualizations')

    # Total streams over time
    st.subheader('Total Streams Over Time')
    plot_total_streams(data)

    # Average streams per song over time
    st.subheader('Average Streams Per Song Over Time')
    plot_avg_streams(data)

    # Distribution of streams
    st.subheader('Distribution of Streams')
    plot_stream_distribution(data)

    # Summary statistics
    st.header('Summary Statistics')
    st.write(data.describe())
else:
    st.write('Please upload a CSV file to analyze the data.')

