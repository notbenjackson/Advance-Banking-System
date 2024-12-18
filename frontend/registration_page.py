import streamlit as st
from src.services.registration_service import RegistrationService

def render_registration_page(registration_service: RegistrationService):
    """
    User registration page
    """
    st.title("Create New Account")
    
    with st.form("registration_form"):
        # Registration fields
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        register_button = st.form_submit_button("Register")

        if register_button:
            # Prepare registration data
            registration_data = {
                'username': username,
                'email': email,
                'password': password,
                'confirm_password': confirm_password
            }

            # Attempt registration
            result = registration_service.register_user(registration_data)

            if result['success']:
                st.success("Registration Successful! You can now log in.")
            else:
                # Display validation errors
                for field, error in result.get('errors', {}).items():
                    st.error(f"{field.capitalize()}: {error}")