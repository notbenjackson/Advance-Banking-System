import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

class DataVisualizations:
    """
    Comprehensive data visualization class for banking system
    """
    
    @staticmethod
    def spending_breakdown(transactions_df):
        """
        Create a pie chart of spending by category
        
        Args:
            transactions_df (pd.DataFrame): DataFrame with transaction data
        
        Returns:
            plotly figure: Pie chart of spending breakdown
        """
        # Filter for expenses (negative amounts)
        expenses = transactions_df[transactions_df['Amount'] < 0]
        category_spending = expenses.groupby('Category')['Amount'].sum().abs()
        
        fig = px.pie(
            values=category_spending.values, 
            names=category_spending.index, 
            title='Spending Breakdown by Category'
        )
        return fig
    
    @staticmethod
    def income_vs_expenses_trend(transactions_df):
        """
        Create a line chart showing income vs expenses trend
        
        Args:
            transactions_df (pd.DataFrame): DataFrame with transaction data
        
        Returns:
            plotly figure: Line chart of income and expenses
        """
        # Group transactions by month and categorize
        monthly_transactions = transactions_df.groupby([
            pd.Grouper(key='Date', freq='M'), 
            transactions_df['Amount'].apply(lambda x: 'Income' if x > 0 else 'Expense')
        ])['Amount'].sum().unstack()
        
        # Create line chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=monthly_transactions.index, 
            y=monthly_transactions['Income'], 
            mode='lines+markers',
            name='Income',
            line=dict(color='green')
        ))
        fig.add_trace(go.Scatter(
            x=monthly_transactions.index, 
            y=abs(monthly_transactions['Expense']), 
            mode='lines+markers',
            name='Expenses',
            line=dict(color='red')
        ))
        
        fig.update_layout(
            title='Monthly Income vs Expenses',
            xaxis_title='Month',
            yaxis_title='Amount ($)'
        )
        
        return fig
    
    @staticmethod
    def account_growth_projection(initial_balance=10000, monthly_saving=500, months=12):
        """
        Create a projection of account growth
        
        Args:
            initial_balance (float): Starting account balance
            monthly_saving (float): Monthly contribution
            months (int): Number of months to project
        
        Returns:
            plotly figure: Line chart of account growth projection
        """
        # Create projection data
        months_list = list(range(months))
        balances = [initial_balance + (monthly_saving * month) for month in months_list]
        
        # Add some simulated investment growth (assuming 6% annual return)
        growth_rates = [1 + (0.06/12 * month) for month in months_list]
        projected_balances = [bal * rate for bal, rate in zip(balances, growth_rates)]
        
        projection_df = pd.DataFrame({
            'Month': months_list,
            'Projected Balance': projected_balances
        })
        
        # Create line chart
        fig = px.line(
            projection_df, 
            x='Month', 
            y='Projected Balance', 
            title='Account Growth Projection',
            labels={'Projected Balance': 'Balance ($)'}
        )
        
        return fig
    
    @staticmethod
    def credit_score_simulation(current_score=700, months=12):
        """
        Simulate potential credit score changes
        
        Args:
            current_score (int): Starting credit score
            months (int): Number of months to simulate
        
        Returns:
            plotly figure: Line chart of potential credit score changes
        """
        # Simulate credit score changes with random variations
        np.random.seed(42)  # For reproducibility
        
        # Create variations that trend towards improvement
        variations = np.random.normal(
            loc=2,  # Slight positive trend
            scale=5,  # Variation scale
            size=months
        )
        
        credit_scores = [
            min(850, max(300, current_score + int(variation))) 
            for variation in variations
        ]
        
        # Create line chart
        fig = go.Figure(data=go.Scatter(
            x=list(range(months)), 
            y=credit_scores, 
            mode='lines+markers',
            line=dict(color='blue')
        ))
        
        fig.update_layout(
            title='Potential Credit Score Progression',
            xaxis_title='Months',
            yaxis_title='Credit Score',
            yaxis=dict(range=[min(credit_scores)-50, max(credit_scores)+50])
        )
        
        return fig

def generate_sample_transactions():
    """
    Generate sample transaction data for visualization
    
    Returns:
        pd.DataFrame: Sample transactions with categories
    """
    # Generate date range
    dates = pd.date_range(start='2024-01-01', periods=100)
    
    # Define categories with their probability of occurrence
    categories = {
        'Groceries': (-250, -50, 0.2),
        'Dining Out': (-100, -30, 0.15),
        'Entertainment': (-150, -50, 0.1),
        'Utilities': (-200, -100, 0.1),
        'Transportation': (-80, -20, 0.1),
        'Shopping': (-300, -50, 0.1),
        'Salary': (2000, 5000, 0.05),
        'Freelance': (500, 2000, 0.05),
        'Investments': (100, 1000, 0.1)
    }
    
    # Lists to store data
    data_list = []
    
    # Generate transactions
    for date in dates:
        # Randomly select a category
        category, (min_val, max_val, prob) = np.random.choice(
            list(categories.items()), 
            p=[cat[2] for cat in categories.values()]
        )
        
        # Generate amount
        amount = np.random.uniform(min_val, max_val)
        
        # Add to data list
        data_list.append({
            'Date': date,
            'Amount': amount,
            'Category': category
        })
    
    # Create DataFrame
    return pd.DataFrame(data_list)

def render_data_visualizations():
    """
    Render various data visualizations for the banking system
    
    This function can be imported and called directly in a Streamlit app
    """
    st.title("📊 Advanced Data Visualizations")
    
    # Generate sample transaction data
    transactions_df = generate_sample_transactions()
    
    # Tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs([
        "Spending Breakdown", 
        "Income vs Expenses", 
        "Account Growth", 
        "Credit Score Projection"
    ])
    
    with tab1:
        st.header("Spending Breakdown")
        fig1 = DataVisualizations.spending_breakdown(transactions_df)
        st.plotly_chart(fig1, use_container_width=True)
        
        # Some additional insights
        st.subheader("Spending Insights")
        expense_summary = transactions_df[transactions_df['Amount'] < 0].groupby('Category')['Amount'].sum()
        st.table(expense_summary.abs().sort_values(ascending=False))
    
    with tab2:
        st.header("Income vs Expenses Trend")
        fig2 = DataVisualizations.income_vs_expenses_trend(transactions_df)
        st.plotly_chart(fig2, use_container_width=True)
        
        # Calculate total income and expenses
        total_income = transactions_df[transactions_df['Amount'] > 0]['Amount'].sum()
        total_expenses = abs(transactions_df[transactions_df['Amount'] < 0]['Amount'].sum())
        st.metric(label="Total Income", value=f"${total_income:,.2f}")
        st.metric(label="Total Expenses", value=f"${total_expenses:,.2f}")
    
    with tab3:
        st.header("Account Growth Projection")
        # Allow user to customize projection parameters
        initial_balance = st.number_input(
            "Initial Balance", 
            min_value=0, 
            value=10000, 
            step=1000
        )
        monthly_saving = st.number_input(
            "Monthly Saving", 
            min_value=0, 
            value=500, 
            step=100
        )
        projection_months = st.slider(
            "Projection Months", 
            min_value=1, 
            max_value=60, 
            value=12
        )
        
        fig3 = DataVisualizations.account_growth_projection(
            initial_balance, 
            monthly_saving, 
            projection_months
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with tab4:
        st.header("Credit Score Projection")
        # Allow user to customize credit score simulation
        current_score = st.number_input(
            "Current Credit Score", 
            min_value=300, 
            max_value=850, 
            value=700
        )
        simulation_months = st.slider(
            "Simulation Months", 
            min_value=1, 
            max_value=36, 
            value=12
        )
        
        fig4 = DataVisualizations.credit_score_simulation(
            current_score, 
            simulation_months
        )
        st.plotly_chart(fig4, use_container_width=True)
