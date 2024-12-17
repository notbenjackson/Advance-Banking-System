import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def render_dashboard():
    """
    Render the main dashboard with financial insights and visualizations
    """
    st.title("🏦 Banking Dashboard")
    
    # Account Summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Balance", "$10,500.25", "+$250 (2.4%)")
    with col2:
        st.metric("Total Savings", "$45,000", "+$1,200 YTD")
    with col3:
        st.metric("Credit Score", "742", "Excellent")
    
    # Transaction Breakdown
    st.subheader("Recent Transaction Categories")
    
    # Sample transaction data
    transaction_data = pd.DataFrame({
        'Category': ['Groceries', 'Utilities', 'Dining', 'Shopping', 'Miscellaneous'],
        'Amount': [450, 280, 350, 220, 150]
    })
    
    # Pie chart for transaction categories
    fig = px.pie(transaction_data, values='Amount', names='Category', title='Spending by Category')
    st.plotly_chart(fig)
    
    # Recent Transactions
    st.subheader("Recent Transactions")
    transactions = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=5),
        'Description': ['Salary Deposit', 'Electricity Bill', 'Restaurant Dinner', 
                        'Online Shopping', 'Grocery Store'],
        'Amount': [5000, -280, -85, -150, -120]
    })
    
    # Color-coded transaction table
    def color_amount(val):
        color = 'green' if val > 0 else 'red'
        return f'color: {color}'
    
    styled_transactions = transactions.style.applymap(color_amount, subset=['Amount'])
    st.dataframe(styled_transactions)
    
    # Account Growth Projection
    st.subheader("Account Growth Projection")
    projection_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Projected Balance': [10000, 11000, 12500, 13800, 15200, 16700]
    })
    
    fig_line = px.line(projection_data, x='Month', y='Projected Balance', title='Account Balance Projection')
    st.plotly_chart(fig_line)