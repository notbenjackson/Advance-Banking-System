import main as st
from src.services.account_service import AccountService

def dashboard():
    st.title(f"Welcome, {st.session_state['username']}")

    account_service = AccountService()
    accounts = account_service.get_user_accounts(st.session_state["username"])
    
    st.header("Your Accounts")
    for account in accounts:
        with st.expander(f"Account {account.account_number}"):
            st.wrtie(f"Balance: Rp{account.balance}")
            st.write(f"Type: {account.account_type}")