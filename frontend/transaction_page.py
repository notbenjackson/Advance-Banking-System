import streamlit as st
from src.services.transaction_service import TransactionService
from src.services.account_service import AccountService

def transaction_page():
    st.title("Transfer Funds")

    # Initialize services
    account_service = AccountService()
    transaction_service = TransactionService()

    # Verify user is logged in
    if 'username' not in st.session_state:
        st.error("Please log in first")
        return

    # Fetch user accounts
    accounts = account_service.get_user_accounts(st.session_state['username'])
    
    # Prepare account options
    account_options = [str(account.account_number) for account in accounts]

    # Create columns for layout
    col1, col2 = st.columns(2)

    with col1:
        from_account = st.selectbox("From Account", 
                                    account_options, 
                                    key="from_account")
    
    with col2:
        # Dynamically filter out the source account from destination options
        to_account_options = [acc for acc in account_options if acc != from_account]
        to_account = st.selectbox("To Account", 
                                  to_account_options, 
                                  key="to_account")

    # Amount input with validation
    amount = st.number_input("Amount", 
                              min_value=0.01, 
                              step=1.00, 
                              format="%.2f",
                              key="transfer_amount")

    # Transfer button
    if st.button("Transfer Funds", key="transfer_button"):
        try:
            # Validate inputs
            if not from_account or not to_account:
                st.error("Please select both source and destination accounts")
                return

            if amount <= 0:
                st.error("Transfer amount must be greater than zero")
                return

            # Perform transfer
            result = transaction_service.transfer(
                from_account,
                to_account,
                amount
            )

            # Handle transfer result
            if result:
                st.success("Transaction Successful!")
                # Optional: Clear input fields after successful transfer
                st.session_state['from_account'] = None
                st.session_state['to_account'] = None
                st.session_state['transfer_amount'] = 0.0
            else:
                st.error("Transaction Failed. Please check your account balance and try again.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
