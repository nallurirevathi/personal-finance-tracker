"""
Sidebar filter components
"""

import streamlit as st


def render_sidebar(df):
    """Render sidebar with filters"""
    st.sidebar.header("🔍 Filters")
    
    # Transaction type filter
    transaction_type = st.sidebar.selectbox(
        "Transaction Type",
        ['All', 'Expense', 'Income', 'Transfer-In', 'Transfer-Out']
    )
    
    # Category filter
    categories = ['All'] + sorted(df['Category'].dropna().unique().tolist())
    selected_category = st.sidebar.selectbox("Select Category", categories)
    
    # Year filter
    years = ['All'] + sorted(df['Year'].unique().tolist(), reverse=True)
    selected_year = st.sidebar.selectbox("Select Year", years)
    
    return transaction_type, selected_category, selected_year
