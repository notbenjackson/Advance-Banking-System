import streamlit as st
import pandas as pd

def account_dashboard():
    st.title("Banking Dashboard")
    
    # Fetch account data
    account_data = get_account_data()
    
    # Display account summary
    st.header("Account Summary")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Total Balance", value=f"${account_data['balance']:,.2f}")
    
    with col2:
        st.metric(label="Recent Transactions", value=len(account_data['transactions']))
    
    # Transaction history
    st.subheader("Recent Transactions")
    transactions_df = pd.DataFrame(account_data['transactions'])
    st.dataframe(transactions_df)
    
    # Visualization
    st.subheader("Spending Breakdown")
    spending_chart = create_spending_chart(transactions_df)
    st.plotly_chart(spending_chart)

def main():
    st.set_page_config(page_title="Banking System", page_icon=":bank:")
    
    # Authentication
    if not st.session_state.get('logged_in', False):
        login_page()
    else:
        account_dashboard()

if __name__ == "__main__":
    main()