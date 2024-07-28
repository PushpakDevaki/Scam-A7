import streamlit as st
import pandas as pd

# Initialize session state for storing data
if 'finance_data' not in st.session_state:
    st.session_state.finance_data = pd.DataFrame(columns=['Date', 'Type', 'Category', 'Amount'])

# Function to add a new entry
def add_entry(date, entry_type, category, amount):
    new_entry = pd.DataFrame({
        'Date': [date],
        'Type': [entry_type],
        'Category': [category],
        'Amount': [amount]
    })
    st.session_state.finance_data = pd.concat([st.session_state.finance_data, new_entry], ignore_index=True)

# Streamlit App
def main():
    st.title("Personal Finance Tracker")

    with st.form("entry_form"):
        date = st.date_input("Date")
        entry_type = st.selectbox("Type", ["Income", "Expense"])
        category = st.text_input("Category")
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        submit = st.form_submit_button("Add Entry")
        
        if submit:
            add_entry(date, entry_type, category, amount)
            st.success("Entry added successfully!")

    st.subheader("Finance Data")
    st.dataframe(st.session_state.finance_data)

    if not st.session_state.finance_data.empty:
        st.subheader("Summary")
        summary = st.session_state.finance_data.groupby(['Type']).sum()['Amount']
        st.write(summary)
        
        st.subheader("Expense Breakdown by Category")
        expense_data = st.session_state.finance_data[st.session_state.finance_data['Type'] == 'Expense']
        expense_summary = expense_data.groupby(['Category']).sum()['Amount']
        st.bar_chart(expense_summary)

if __name__ == "__main__":
    main()
