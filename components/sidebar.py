import streamlit as st
import streamlit.components.v1 as components

def create_sidebar():
    """
    Create a sidebar for navigation in the banking system
    
    Returns:
        str: Selected page name
    """
    st.sidebar.title("🏦 Advanced Banking")
    
    # User information display
    st.sidebar.header("Welcome, User")
    st.sidebar.write("Account Balance: $10,000")
    st.sidebar.write("Last Login: Today")
    
    # Navigation options
    page = st.sidebar.radio("Navigate", [
        "Dashboard", 
        "Transactions", 
        "Account Management", 
        "Support Tickets"
    ])
    
    return page