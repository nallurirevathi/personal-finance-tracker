"""
Table rendering components
"""

import streamlit as st
from config import RECENT_TRANSACTIONS, TOP_EXPENSES


def render_recent_transactions(filtered_df):
    """Render recent transactions table"""
    st.subheader("📋 Recent Transactions")
    recent_df = filtered_df.sort_values('Date', ascending=False).head(RECENT_TRANSACTIONS)
    display_cols = ['Date', 'Category', 'Subcategory', 'Amount', 'Mode', 'Income/Expense', 'Note']
    st.dataframe(
        recent_df[display_cols].style.format({'Amount': '₹{:,.2f}'}),
        use_container_width=True,
        hide_index=True
    )


def render_top_expenses_and_summary(expenses_df):
    """Render top expenses and category summary side by side"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔝 Top 10 Highest Expenses")
        top_expenses = expenses_df.nlargest(TOP_EXPENSES, 'Amount')[
            ['Date', 'Category', 'Amount', 'Note']
        ]
        st.dataframe(
            top_expenses.style.format({'Amount': '₹{:,.2f}'}),
            use_container_width=True,
            hide_index=True
        )
    
    with col2:
        st.subheader("📊 Category Summary")
        category_summary = expenses_df.groupby('Category')['Amount'].agg(
            ['sum', 'count', 'mean']
        ).sort_values('sum', ascending=False).head(TOP_EXPENSES)
        category_summary.columns = ['Total', 'Count', 'Average']
        st.dataframe(
            category_summary.style.format({'Total': '₹{:,.0f}', 'Average': '₹{:,.0f}'}),
            use_container_width=True
        )
