import streamlit as st
import hashlib

def hash_password(password):
    """
    Hash the password using SHA-256
    
    Args:
        password (str): Plain text password
    
    Returns:
        str: Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user():
    """
    Authenticate user with username and password
    
    Returns:
        bool: Authentication result
    """
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Simple authentication (in a real system, use secure backend authentication)
    if st.button("Login"):
        if username and password:
            # Simulate password check (replace with actual backend authentication)
            hashed_input = hash_password(password)
            
            # Mock credentials (replace with actual backend verification)
            mock_username = "admin"
            mock_password_hash = hash_password("password123")
            
            if username == mock_username and hashed_input == mock_password_hash:
                return True
            else:
                st.error("Invalid username or password")
        else:
            st.warning("Please enter username and password")
    
    return False