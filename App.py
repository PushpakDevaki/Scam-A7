import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize data storage
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Date', 'Type', 'Category', 'Amount'])

# Function to add new data
def add_data(date, trans_type, category, amount):
    new_data = {'Date': date, 'Type': trans_type, 'Category': category, 'Amount': amount}
    st.session_state['data'] = st.session_state['data'].append(new_data, ignore_index=True)

# App title
st.title('Finance Tracker')

# Input form
st.header('Log Your Financial Data')
with st.form(key='finance_form'):
    date = st.date_input('Date')
    trans_type = st.selectbox('Type', ['Income', 'Expense'])
    category = st.text_input('Category')
    amount = st.number_input('Amount', min_value=0.0, step=0.01)
    submit_button = st.form_submit_button(label='Add Data')
    if submit_button:
        add_data(date, trans_type, category, amount)
        st.success('Data added successfully!')

# Display data
st.header('Financial Data')
st.write(st.session_state['data'])

# Visualizations
if not st.session_state['data'].empty:
    st.header('Visualizations')

    # Total income and expenses over time
    st.subheader('Income and Expenses Over Time')
    income_data = st.session_state['data'][st.session_state['data']['Type'] == 'Income']
    expense_data = st.session_state['data'][st.session_state['data']['Type'] == 'Expense']
    
    plt.figure(figsize=(10, 5))
    plt.plot(income_data['Date'], income_data['Amount'], label='Income', marker='o', color='green')
    plt.plot(expense_data['Date'], expense_data['Amount'], label='Expense', marker='o', color='red')
    plt.title('Income and Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.legend()
    st.pyplot(plt)

    # Expenses by category
    st.subheader('Expenses by Category')
    expense_by_category = expense_data.groupby('Category')['Amount'].sum()
    st.bar_chart(expense_by_category)

    # Summary statistics
    st.header('Summary Statistics')
    st.write(st.session_state['data'].describe())
else:
    st.write('No data available. Please log your financial data.')
