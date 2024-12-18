import streamlit as st
import traceback
from src.services.authentication_service import AuthenticationService
from src.services.registration_service import RegistrationService

class BankingApp:
    def __init__(self):
        # Configure page settings
        st.set_page_config(
            page_title="Banking System", 
            page_icon=":bank:", 
            layout="wide"
        )

        # Initialize services
        self.auth_service = AuthenticationService()
        self.registration_service = RegistrationService(self.auth_service)

    def run(self):
        # Initialize session state
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False

        # If user is not logged in
        if not st.session_state['logged_in']:
            page = st.sidebar.selectbox("Navigation", ["Login", "Register"])

            if page == "Login":
                from frontend.login_page import render_login_page
                render_login_page(self.auth_service)
            else:
                from frontend.registration_page import render_registration_page
                render_registration_page(self.registration_service)
        else:
            # Logged-in user navigation
            menu = st.sidebar.radio("Menu", ["Dashboard", "Transactions", "Account Management", "Logout"])

            if menu == "Dashboard":
                from frontend.dashboard import dashboard
                dashboard()
            elif menu == "Transactions":
                from frontend.transaction_page import transaction_page
                transaction_page()
            elif menu == "Account Management":
                from frontend.account_management import account_management
                account_management()
            elif menu == "Logout":
                self._logout()

    def _logout(self):
        """
        Logout user and reset session state
        """
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

def main():
    """
    Entry point for the banking application
    """
    try:
        app = BankingApp()
        app.run()
    except Exception as e:
        st.error("An unexpected error occurred. Please check the logs.")
        st.write(traceback.format_exc())

if __name__ == "__main__":
    main()
