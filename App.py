import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load and process data
@st.cache
def load_data(file):
    data = pd.read_csv(file)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

# Function to plot total points over time
def plot_total_points(data):
    total_points = data.groupby('Date')['Points'].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(total_points.index, total_points.values, marker='o')
    plt.title('Total Points Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Points')
    st.pyplot(plt)

# Function to plot average points per game over time
def plot_avg_points(data):
    avg_points = data.groupby('Date')['Points'].mean()
    plt.figure(figsize=(10, 5))
    plt.plot(avg_points.index, avg_points.values, marker='o', color='orange')
    plt.title('Average Points Per Game Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Points')
    st.pyplot(plt)

# Function to plot distribution of points
def plot_points_distribution(data):
    plt.figure(figsize=(10, 5))
    plt.hist(data['Points'], bins=30, color='purple', edgecolor='black')
    plt.title('Distribution of Points')
    plt.xlabel('Points')
    plt.ylabel('Frequency')
    st.pyplot(plt)

# App title
st.title('Sports Analytics Platform')

# File uploader
uploaded_file = st.file_uploader('Upload your CSV file', type=['csv'])

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write(data.head())

    st.header('Visualizations')

    # Total points over time
    st.subheader('Total Points Over Time')
    plot_total_points(data)

    # Average points per game over time
    st.subheader('Average Points Per Game Over Time')
    plot_avg_points(data)

    # Distribution of points
    st.subheader('Distribution of Points')
    plot_points_distribution(data)

    # Summary statistics
    st.header('Summary Statistics')
    st.write(data.describe())
else:
    st.write('Please upload a CSV file to analyze the data.')

