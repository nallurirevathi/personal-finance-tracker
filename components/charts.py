"""
Chart rendering components
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from visualizations import (
    create_category_pie_chart,
    create_mode_bar_chart,
    create_monthly_line_chart,
    create_prediction_chart,
    create_day_of_week_chart
)
from utils import format_currency, calculate_percentage_change
from config import TOP_CATEGORIES, DAYS_ORDER


def render_category_and_mode_charts(expenses_df):
    """Render category and payment mode charts side by side"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Spending by Category")
        category_totals = expenses_df.groupby('Category')['Amount'].sum().sort_values(
            ascending=False
        ).head(TOP_CATEGORIES)
        fig = create_category_pie_chart(category_totals)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💳 Payment Mode Distribution")
        mode_totals = expenses_df.groupby('Mode')['Amount'].sum().sort_values(ascending=False)
        fig = create_mode_bar_chart(mode_totals)
        st.plotly_chart(fig, use_container_width=True)


def render_monthly_trend(expenses_df):
    """Render monthly spending trend chart"""
    st.subheader("📈 Monthly Spending Trend")
    monthly_expenses = expenses_df.groupby('Month')['Amount'].sum().reset_index()
    monthly_expenses.columns = ['Month', 'Amount']
    fig = create_monthly_line_chart(monthly_expenses)
    st.plotly_chart(fig, use_container_width=True)


def render_prediction_section(expenses_df):
    """Render AI prediction section"""
    st.subheader("🔮 AI-Powered Expense Prediction")
    
    monthly_data = expenses_df.groupby('Month')['Amount'].sum().reset_index()
    monthly_data['Month_Num'] = np.arange(len(monthly_data))
    
    # Train model
    X = monthly_data[['Month_Num']]
    y = monthly_data['Amount']
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict
    next_month_num = len(monthly_data)
    predicted_expense = model.predict([[next_month_num]])[0]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = create_prediction_chart(monthly_data, predicted_expense)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Prediction Results")
        st.metric("Predicted Next Month", format_currency(predicted_expense))
        
        last_month = monthly_data['Amount'].iloc[-1]
        change = predicted_expense - last_month
        change_pct = calculate_percentage_change(predicted_expense, last_month)
        
        st.metric("Change from Last Month", format_currency(change), f"{change_pct:+.1f}%")
        st.info(f"📅 Last Month: {format_currency(last_month)}")


def render_day_of_week_chart(expenses_df):
    """Render day of week spending chart"""
    st.subheader("📅 Spending by Day of Week")
    day_spending = expenses_df.groupby('DayOfWeek')['Amount'].sum().reindex(DAYS_ORDER)
    fig = create_day_of_week_chart(day_spending)
    st.plotly_chart(fig, use_container_width=True)
