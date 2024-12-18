import streamlit as st
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
        # Import pages here to avoid circular imports
        from frontend.login_page import render_login_page
        from frontend.registration_page import render_registration_page
        from frontend.dashboard import dashboard
        from frontend.transaction_page import transaction_page
        from frontend.account_management import account_management

        # Initialize session state
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False

        if not st.session_state['logged_in']:
            # Show login or registration page
            page = st.sidebar.selectbox(
                "Navigation", 
                ["Login", "Register"]
            )
            
            if page == "Login":
                render_login_page(self.auth_service)
            else:
                render_registration_page(self.registration_service)
        else:
            # Logged-in user navigation
            menu = st.sidebar.radio(
                "Menu", 
                [
                    "Dashboard", 
                    "Transactions", 
                    "Account Management", 
                    "Logout"
                ]
            )

            # Render appropriate page based on menu selection
            if menu == "Dashboard":
                dashboard()
            elif menu == "Transactions":
                transaction_page()
            elif menu == "Account Management":
                account_management()
            elif menu == "Logout":
                self._logout()

    def _logout(self):
        """
        Logout user and reset session state
        """
        st.session_state['logged_in'] = False
        st.experimental_rerun()

def main():
    """
    Entry point for the banking application
    """
    try:
        app = BankingApp()
        app.run()
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()