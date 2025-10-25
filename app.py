"""
Main Streamlit Application
Personal Finance Tracker - AI-Powered Dashboard
"""

import streamlit as st
import warnings
warnings.filterwarnings('ignore')

# Import configurations
from config import PAGE_TITLE, PAGE_ICON, LAYOUT, CUSTOM_CSS

# Import data functions
from data_loader import load_data, filter_data, get_expenses_only, get_summary_stats

# Import all components
from components import (
    render_sidebar,
    render_metrics,
    render_category_and_mode_charts,
    render_monthly_trend,
    render_prediction_section,
    render_day_of_week_chart,
    render_recent_transactions,
    render_top_expenses_and_summary
)

# Page configuration
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Header
st.markdown(
    f'<p class="main-header">{PAGE_ICON} AI-Powered Personal Finance Tracker</p>',
    unsafe_allow_html=True
)
st.markdown("---")

# Load data
df = load_data()

# Render sidebar and get filter values
transaction_type, selected_category, selected_year = render_sidebar(df)

# Filter data based on selections
filtered_df = filter_data(df, transaction_type, selected_category, selected_year)

# Get expenses only for analysis
expenses_df = get_expenses_only(df)

# Calculate summary statistics
stats = get_summary_stats(filtered_df)

# Render metrics
render_metrics(stats)
st.markdown("---")

# Render charts
render_category_and_mode_charts(expenses_df)
st.markdown("---")

render_monthly_trend(expenses_df)
st.markdown("---")

render_prediction_section(expenses_df)
st.markdown("---")

render_day_of_week_chart(expenses_df)
st.markdown("---")

# Render tables
render_recent_transactions(filtered_df)
st.markdown("---")

render_top_expenses_and_summary(expenses_df)

# Footer
st.markdown("---")
st.markdown(
    """
    <div class='footer'>
        <p>💡 Built with Python, Streamlit, and Machine Learning | Data Analysis Project</p>
    </div>
    """,
    unsafe_allow_html=True
)

#streamlit run app.py
