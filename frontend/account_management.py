import streamlit as st
from src.services.account_service import AccountService

def account_management():
    st.title("Account Management")

    # Initialize account service
    account_service = AccountService()

    # Verify user is logged in
    if 'username' not in st.session_state:
        st.error("Please log in first")
        return

    # Account type selection with more detailed options
    account_type = st.selectbox("Select Account Type", [
        "Savings", 
        "Checking", 
        "Investment", 
        "High-Yield Savings", 
        "Business Checking"
    ])

    # Initial deposit input with improved formatting and validation
    initial_deposit = st.number_input(
        "Initial Deposit", 
        min_value=0.0, 
        step=1.00, 
        format="%.2f",
        help="Minimum initial deposit may vary by account type"
    )

    # Additional account details (optional)
    with st.expander("Additional Account Details"):
        account_nickname = st.text_input("Account Nickname (Optional)")

    # Create account button with enhanced validation
    if st.button("Create Account", key="create_account_btn"):
        # Input validation
        if initial_deposit < 0:
            st.error("Initial deposit cannot be negative")
            return

        try:
            # Attempt to create account
            new_account = account_service.create_account(
                st.session_state['username'],
                account_type,
                initial_deposit,
                account_nickname  # Pass optional nickname
            )

            if new_account:
                st.success("Account Created Successfully!")
                # Optional: Clear input fields or provide additional guidance
                st.balloons()  # Add a celebratory animation
            else:
                st.error("Account Creation Failed. Please try again or contact support.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            # Consider logging the error for debugging
