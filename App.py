import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize data storage
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Date', 'Exercise', 'Calories', 'Weight'])

# Function to add new data
def add_data(date, exercise, calories, weight):
    new_data = {'Date': date, 'Exercise': exercise, 'Calories': calories, 'Weight': weight}
    st.session_state['data'] = st.session_state['data'].append(new_data, ignore_index=True)

# App title
st.title('Health Tracker')

# Input form
st.header('Log Your Health Data')
with st.form(key='health_form'):
    date = st.date_input('Date')
    exercise = st.text_input('Exercise')
    calories = st.number_input('Calories Consumed', min_value=0, step=1)
    weight = st.number_input('Weight (kg)', min_value=0.0, step=0.1)
    submit_button = st.form_submit_button(label='Add Data')
    if submit_button:
        add_data(date, exercise, calories, weight)
        st.success('Data added successfully!')

# Display data
st.header('Health Data')
st.write(st.session_state['data'])

# Visualizations
if not st.session_state['data'].empty:
    st.header('Visualizations')

    # Weight over time
    st.subheader('Weight Over Time')
    plt.figure(figsize=(10, 5))
    plt.plot(st.session_state['data']['Date'], st.session_state['data']['Weight'], marker='o')
    plt.title('Weight Over Time')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    st.pyplot(plt)

    # Calories over time
    st.subheader('Calories Over Time')
    plt.figure(figsize=(10, 5))
    plt.plot(st.session_state['data']['Date'], st.session_state['data']['Calories'], marker='o', color='orange')
    plt.title('Calories Over Time')
    plt.xlabel('Date')
    plt.ylabel('Calories')
    st.pyplot(plt)

    # Exercise entries
    st.subheader('Exercise Entries')
    exercise_counts = st.session_state['data']['Exercise'].value_counts()
    st.bar_chart(exercise_counts)

    # Summary statistics
    st.header('Summary Statistics')
    st.write(st.session_state['data'].describe())

else:
    st.write('No data available. Please log your health data.')
