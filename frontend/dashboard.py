import streamlit as st
from src.services.account_service import AccountService

def dashboard():
    # Verify user is logged in
    if 'username' not in st.session_state:
        st.error("Please log in first")
        return

    # Display personalized welcome
    st.title(f"Welcome, {st.session_state['username']}")

    # Initialize account service
    account_service = AccountService()
    
    # Fetch user accounts
    try:
        accounts = account_service.get_user_accounts(st.session_state["username"])
    except Exception as e:
        st.error(f"Failed to retrieve accounts: {str(e)}")
        return

    # Check if user has any accounts
    if not accounts:
        st.info("You don't have any accounts yet. Create one to get started!")
        return

    # Display accounts section
    st.header("Your Accounts")
    
    # Create a grid layout for accounts
    for account in accounts:
        with st.expander(f"Account {account.account_number}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Balance", f"Rp {account.balance:,.2f}")
            
            with col2:
                st.metric("Account Type", account.account_type)
            
            # Additional account details (optional)
            st.divider()
            
            # Quick actions
            action_col1, action_col2 = st.columns(2)
            
            with action_col1:
                if st.button(f"Transfer from {account.account_number}", key=f"transfer_{account.account_number}"):
                    # TODO: Implement transfer navigation logic
                    st.session_state['selected_account'] = account.account_number
            
            with action_col2:
                if st.button(f"View Details {account.account_number}", key=f"details_{account.account_number}"):
                    # TODO: Implement account details view
                    pass