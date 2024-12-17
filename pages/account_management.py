import streamlit as st
import pandas as pd

def render_account_management():
    """
    Render the account management page with profile, settings, and account details
    """
    st.title("👤 Account Management")
    
    # Tabs for different account management sections
    tab1, tab2, tab3 = st.tabs(["Profile", "Account Details", "Security"])
    
    with tab1:
        st.header("Personal Profile")
        
        # Profile Image Upload
        profile_img = st.file_uploader("Upload Profile Picture", type=['png', 'jpg', 'jpeg'])
        
        # Personal Information Form
        with st.form("profile_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                first_name = st.text_input("First Name", value="John")
                email = st.text_input("Email", value="john.doe@example.com")
                phone = st.text_input("Phone Number", value="+1 (555) 123-4567")
            
            with col2:
                last_name = st.text_input("Last Name", value="Doe")
                address = st.text_area("Address", value="123 Banking Street, Finance City")
            
            submit_button = st.form_submit_button("Update Profile")
            
            if submit_button:
                st.success("Profile Updated Successfully!")
    
    with tab2:
        st.header("Account Details")
        
        # Account Summary
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Account Number", "1234 5678 9012 3456")
        with col2:
            st.metric("Account Type", "Checking")
        with col3:
            st.metric("Account Status", "Active")
        
        # Linked Accounts
        st.subheader("Linked Accounts")
        linked_accounts = pd.DataFrame({
            'Bank': ['Savings Account', 'Credit Card', 'Investment Account'],
            'Account Number': ['XXXX 5678', 'XXXX 9012', 'XXXX 3456'],
            'Balance': ['$45,000', '$2,500', '$75,000']
        })
        st.dataframe(linked_accounts)
        
        # Link New Account Button
        if st.button("Link New Account"):
            with st.form("link_account_form"):
                bank_name = st.text_input("Bank Name")
                account_type = st.selectbox("Account Type", 
                    ["Checking", "Savings", "Credit Card", "Investment", "Other"]
                )
                routing_number = st.text_input("Routing Number")
                account_number = st.text_input("Account Number")
                
                submit_link = st.form_submit_button("Link Account")
                
                if submit_link:
                    st.success("Account Linked Successfully!")
    
    with tab3:
        st.header("Security Settings")
        
        # Change Password Section
        st.subheader("Change Password")
        with st.form("change_password_form"):
            current_password = st.text_input("Current Password", type="password")
            new_password = st.text_input("New Password", type="password")
            confirm_password = st.text_input("Confirm New Password", type="password")
            
            password_change_btn = st.form_submit_button("Change Password")
            
            if password_change_btn:
                if new_password != confirm_password:
                    st.error("Passwords do not match!")
                elif len(new_password) < 8:
                    st.warning("Password must be at least 8 characters long")
                else:
                    st.success("Password Changed Successfully!")
        
        # Two-Factor Authentication
        st.subheader("Two-Factor Authentication")
        two_factor_enabled = st.toggle("Enable Two-Factor Authentication")
        
        if two_factor_enabled:
            st.info("""
            Two-Factor Authentication adds an extra layer of security:
            - A code will be sent to your registered mobile number
            - Each login requires both password and verification code
            - Protects your account from unauthorized access
            """)
            
            # Phone number for 2FA
            phone_number = st.text_input("Mobile Number for 2FA", value="+1 (555) 123-4567")
            
            st.button("Set Up Two-Factor Authentication")
        
        # Security Logs
        st.subheader("Recent Security Activity")
        security_logs = pd.DataFrame({
            'Date': ['2024-01-15 10:30', '2024-01-10 14:45', '2024-01-05 09:20'],
            'Activity': [
                'Login from New Device', 
                'Password Change', 
                'Two-Factor Authentication Enabled'
            ],
            'Location': ['New York, NY', 'Online', 'Online']
        })
        st.dataframe(security_logs)
        
        # Additional Security Options
        st.subheader("Additional Security")
        
        # Device Management
        st.button("Manage Trusted Devices")
        
        # Account Alerts
        st.multiselect("Security Alerts", 
            options=[
                "Unusual Login Activity", 
                "Large Transactions", 
                "Account Changes", 
                "International Transactions"
            ],
            default=["Unusual Login Activity", "Large Transactions"]
        )
        
        # Save Security Preferences
        if st.button("Save Security Preferences"):
            st.success("Security Preferences Updated Successfully!")