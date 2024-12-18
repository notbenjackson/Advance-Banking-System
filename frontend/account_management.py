import main as st
from src.services.account_service import AccountService

def account_management():
    st.title("Account Management")

    account_service = AccountService()

    account_type = st.selectbox("Select Account Type",
                                ["Savings", "Checking", "Investment"])
    
    initial_deposit = st.number_input("Initial Deposit", min_value = 0.0, step = 1)

    if st.button("Create Account"):
        new_account = account_service.create_account(
            st.session_state['username'],
            account_type,
            initial_deposit
        )

        if new_account:
            st.success("Account Created Successfully!")
        else:
            st.error("Account Creation Failed")