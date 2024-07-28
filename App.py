import streamlit as st

# Function to calculate BMI
def calculate_bmi(height, weight):
    bmi = weight / (height / 100) ** 2
    return bmi

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# App title
st.title('BMI Calculator')

# Input fields
height = st.number_input('Enter your height in cm:', min_value=0.0, format="%.2f")
weight = st.number_input('Enter your weight in kg:', min_value=0.0, format="%.2f")

# Calculate BMI when the button is clicked
if st.button('Calculate BMI'):
    if height > 0 and weight > 0:
        bmi = calculate_bmi(height, weight)
        category = bmi_category(bmi)
        st.write(f'Your BMI is: {bmi:.2f}')
        st.write(f'You are classified as: {category}')
    else:
        st.write('Please enter valid height and weight values.')
