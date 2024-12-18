import streamlit as st
from src.services.authentication_service import AuthenticationService

def render_login_page(auth_service):
    """
    Login page with authentication
    """
    st.title("Banking System Login")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            # Attempt authentication
            user = auth_service.authenticate(username, password)

            if user:
                st.session_state['logged_in'] = True
                st.success("Login Successful!")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")

    # Registration link
    st.markdown("Don't have an account? [Register here](./Register)")
