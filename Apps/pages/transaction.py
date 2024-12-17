import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

def render_transactions():
    """
    Render the transactions page with transaction history and filtering
    """
    st.title("💸 Transactions")
    
    # Generate sample transaction data
    def generate_transactions(num_transactions=100):
        transactions = []
        categories = ['Salary', 'Groceries', 'Dining', 'Utilities', 'Shopping', 'Entertainment', 'Transportation', 'Healthcare']
        
        for _ in range(num_transactions):
            transaction = {
                'Date': datetime.now() - timedelta(days=_ * 3),
                'Description': f"Transaction {_+1}",
                'Category': categories[_ % len(categories)],
                'Amount': round((-1 if _ % 3 == 0 else 1) * (_ * 10 + 50), 2)
            }
            transactions.append(transaction)
        
        return pd.DataFrame(transactions)
    
    # Generate and cache transactions
    if 'transactions' not in st.session_state:
        st.session_state.transactions = generate_transactions()
    
    # Filtering
    st.sidebar.header("Transaction Filters")
    
    # Date Range Filter
    start_date = st.sidebar.date_input("Start Date", value=st.session_state.transactions['Date'].min().date())
    end_date = st.sidebar.date_input("End Date", value=st.session_state.transactions['Date'].max().date())
    
    # Category Filter
    categories = st.sidebar.multiselect(
        "Select Categories", 
        options=st.session_state.transactions['Category'].unique(),
        default=st.session_state.transactions['Category'].unique()
    )
    
    # Amount Range
    min_amount = st.sidebar.number_input("Minimum Amount", value=st.session_state.transactions['Amount'].min())
    max_amount = st.sidebar.number_input("Maximum Amount", value=st.session_state.transactions['Amount'].max())
    
    # Apply Filters
    filtered_df = st.session_state.transactions[
        (st.session_state.transactions['Date'].dt.date >= start_date) &
        (st.session_state.transactions['Date'].dt.date <= end_date) &
        (st.session_state.transactions['Category'].isin(categories)) &
        (st.session_state.transactions['Amount'] >= min_amount) &
        (st.session_state.transactions['Amount'] <= max_amount)
    ]
    
    # Transactions Table
    st.subheader("Transaction History")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # Category Spending Breakdown
        st.subheader("Spending by Category")
        category_spending = filtered_df[filtered_df['Amount'] < 0].groupby('Category')['Amount'].sum()
        fig_pie = px.pie(
            values=abs(category_spending.values), 
            names=category_spending.index, 
            title='Spending Distribution'
        )
        st.plotly_chart(fig_pie)
    
    with col2:
        # Monthly Transaction Trend
        st.subheader("Monthly Transaction Trend")
        monthly_transactions = filtered_df.resample('M', on='Date')['Amount'].sum()
        fig_line = px.line(
            x=monthly_transactions.index, 
            y=monthly_transactions.values, 
            labels={'x': 'Month', 'y': 'Total Amount'},
            title='Monthly Transaction Trend'
        )
        st.plotly_chart(fig_line)
    
    # Export Options
    st.sidebar.header("Export Options")
    if st.sidebar.button("Export Transactions to CSV"):
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download Transactions CSV",
            data=csv,
            file_name="transactions.csv",
            mime="text/csv"
        )