"""
Metrics display components
"""

import streamlit as st
from utils import format_currency


def render_metrics(stats):
    """Render key metrics cards"""
    st.subheader("📊 Key Metrics")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("💸 Total Spent", format_currency(stats['total_spent']))
    
    with col2:
        st.metric("📈 Avg Expense", format_currency(stats['avg_expense']))
    
    with col3:
        st.metric("🔝 Highest", format_currency(stats['max_expense']))
    
    with col4:
        st.metric("🧾 Transactions", f"{stats['total_transactions']:,}")
    
    with col5:
        st.metric("📂 Categories", f"{stats['unique_categories']}")
