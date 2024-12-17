import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def render_support_tickets():
    """
    Render the support tickets page with ticket creation and tracking
    """
    st.title("🆘 Support Tickets")
    
    # Generate sample ticket data
    def generate_sample_tickets(num_tickets=20):
        statuses = ['Open', 'In Progress', 'Resolved', 'Closed']
        priorities = ['Low', 'Medium', 'High', 'Urgent']
        departments = ['Billing', 'Technical Support', 'Account Management', 'Fraud Prevention']
        
        tickets = []
        for i in range(num_tickets):
            ticket = {
                'Ticket ID': f'TICK-{1000 + i}',
                'Date Created': datetime.now() - timedelta(days=i),
                'Subject': f'Support Request {i+1}',
                'Status': statuses[i % len(statuses)],
                'Priority': priorities[i % len(priorities)],
                'Department': departments[i % len(departments)]
            }
            tickets.append(ticket)
        
        return pd.DataFrame(tickets)
    
    # Cached ticket data
    if 'support_tickets' not in st.session_state:
        st.session_state.support_tickets = generate_sample_tickets()
    
    # Ticket Creation Section
    st.header("Create New Support Ticket")
    with st.form("create_ticket_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            ticket_subject = st.text_input("Subject")
            department = st.selectbox("Department", [
                "Billing", 
                "Technical Support", 
                "Account Management", 
                "Fraud Prevention"
            ])
        
        with col2:
            priority = st.selectbox("Priority", [
                "Low", 
                "Medium", 
                "High", 
                "Urgent"
            ])
        
        ticket_description = st.text_area("Describe Your Issue")
        
        submit_ticket = st.form_submit_button("Submit Ticket")
        
        if submit_ticket:
            if ticket_subject and ticket_description:
                new_ticket = {
                    'Ticket ID': f'TICK-{len(st.session_state.support_tickets) + 1000}',
                    'Date Created': datetime.now(),
                    'Subject': ticket_subject,
                    'Status': 'Open',
                    'Priority': priority,
                    'Department': department
                }
                
                # Add new ticket to the dataframe
                new_ticket_df = pd.DataFrame([new_ticket])
                st.session_state.support_tickets = pd.concat([
                    st.session_state.support_tickets, 
                    new_ticket_df
                ], ignore_index=True)
                
                st.success(f"Ticket {new_ticket['Ticket ID']} Created Successfully!")
            else:
                st.error("Please fill in all required fields")
    
    # Ticket Filtering
    st.sidebar.header("Ticket Filters")
    
    # Status Filter
    status_filter = st.sidebar.multiselect(
        "Filter by Status", 
        options=st.session_state.support_tickets['Status'].unique(),
        default=st.session_state.support_tickets['Status'].unique()
    )
    
    # Priority Filter
    priority_filter = st.sidebar.multiselect(
        "Filter by Priority", 
        options=st.session_state.support_tickets['Priority'].unique(),
        default=st.session_state.support_tickets['Priority'].unique()
    )
    
    # Department Filter
    department_filter = st.sidebar.multiselect(
        "Filter by Department", 
        options=st.session_state.support_tickets['Department'].unique(),
        default=st.session_state.support_tickets['Department'].unique()
    )
    
    # Apply Filters
    filtered_tickets = st.session_state.support_tickets[
        (st.session_state.support_tickets['Status'].isin(status_filter)) &
        (st.session_state.support_tickets['Priority'].isin(priority_filter)) &
        (st.session_state.support_tickets['Department'].isin(department_filter))
    ]
    
    # Ticket Summary
    st.header("Your Support Tickets")
    
    # Color-coded Status
    def color_status(status):
        color_map = {
            'Open': 'red',
            'In Progress': 'orange',
            'Resolved': 'green',
            'Closed': 'blue'
        }
        return color_map.get(status, 'black')
    
    # Styled DataFrame
    styled_tickets = filtered_tickets.style.apply(
        lambda x: [f'color: {color_status(val)}' for val in x], 
        subset=['Status']
    )
    
    st.dataframe(styled_tickets, use_container_width=True)
    
    # Export Options
    if st.sidebar.button("Export Tickets to CSV"):
        csv = filtered_tickets.to_csv(index=False)
        st.download_button(
            label="Download Tickets CSV",
            data=csv,
            file_name="support_tickets.csv",
            mime="text/csv"
        )
    
    # Ticket Details Expander
    with st.expander("View Ticket Details"):
        selected_ticket = st.selectbox(
            "Select a Ticket", 
            filtered_tickets['Ticket ID'].tolist()
        )
        
        if selected_ticket:
            ticket_details = filtered_tickets[filtered_tickets['Ticket ID'] == selected_ticket]
            st.table(ticket_details)