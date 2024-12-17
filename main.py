import streamlit as st
from pages.dashboard import render_dashboard
from pages.transaction import render_transactions
from pages.account_management import render_account_management
from pages.support_tickets import render_support_tickets
from components.sidebar import create_sidebar
from components.authentication import authenticate_user

def main():
    # Set page configuration
    st.set_page_config(page_title="Advanced Banking System", page_icon=":bank:", layout="wide")
    
    # Authentication
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    # Login Page
    if not st.session_state.authenticated:
        st.title("Advanced Banking System")
        st.subheader("Login")
        
        # Authentication component
        login_result = authenticate_user()
        
        if login_result:
            st.session_state.authenticated = True
            st.success("Login Successful!")
            st.experimental_rerun()
    
    # Main Application
    if st.session_state.authenticated:
        # Create sidebar for navigation
        page = create_sidebar()
        
        # Render appropriate page based on sidebar selection
        if page == "Dashboard":
            render_dashboard()
        elif page == "Transactions":
            render_transactions()
        elif page == "Account Management":
            render_account_management()
        elif page == "Support Tickets":
            render_support_tickets()
        
        # Logout functionality
        if st.sidebar.button("Logout"):
            st.session_state.authenticated = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()