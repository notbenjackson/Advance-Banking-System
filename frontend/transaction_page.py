import main as st
from src.services.transaction_service import TransactionService
from src.services.account_service import AccountService

def transaction_page():
    st.title("Transactions")

    account_service = AccountService()
    transaction_service = TransactionService()

    accounts = account_service.get_user_accounts(st.session_state['username'])

    from_account = st.selectbox("From Account", 
                                [str(account.account_number) for account in accounts])
    
    to_account = st.selectbox("To Account Number")
    amount = st.number_input("Ammount", min_value=0.0, step = 1)

    if st.button("Transfer"):
        result = transaction_service.transfer(
            from_account,
            to_account,
            amount
        )

        if result:
            st.success("Transaction Successful!")
        else:
            st.error("Transaction Failed")