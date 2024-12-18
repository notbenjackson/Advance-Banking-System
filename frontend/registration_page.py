import streamlit as st
from src.services.registration_service import RegistrationService

class RegistrationService:
    def __init__(self):
        # In-memory user database
        self.users = {}

    def register_user(self, registration_data):
        username = registration_data['username']
        email = registration_data['email']
        password = registration_data['password']
        confirm_password = registration_data['confirm_password']

        errors = {}

        # Validate fields
        if not username or not email or not password:
            errors['general'] = "All fields are required"
        if password != confirm_password:
            errors['password'] = "Passwords do not match"
        if username in self.users:
            errors['username'] = "Username already exists"

        if errors:
            return {'success': False, 'errors': errors}

        # Save user
        self.users[username] = {'email': email, 'password': password}
        return {'success': True}

class AuthenticationService:
    def __init__(self, registration_service):
        self.registration_service = registration_service

    def authenticate(self, username, password):
        # Retrieve user and validate credentials
        user = self.registration_service.users.get(username)
        if not user:
            return False
        return user['password'] == password


def render_registration_page(registration_service):
    """
    User registration page
    """
    st.title("Create New Account")

    with st.form("registration_form"):
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