"""
Chart and visualization functions
"""

import plotly.express as px
import plotly.graph_objects as go
from config import CHART_COLORS


def create_category_pie_chart(category_totals):
    """Create pie chart for category-wise spending"""
    fig = px.pie(
        values=category_totals.values,
        names=category_totals.index,
        hole=0.4,
        color_discrete_sequence=CHART_COLORS
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=400)
    return fig


def create_mode_bar_chart(mode_totals):
    """Create bar chart for payment mode distribution"""
    fig = px.bar(
        x=mode_totals.index,
        y=mode_totals.values,
        labels={'x': 'Payment Mode', 'y': 'Amount (₹)'},
        color=mode_totals.values,
        color_continuous_scale='Blues'
    )
    fig.update_layout(showlegend=False, height=400)
    return fig


def create_monthly_line_chart(monthly_expenses):
    """Create line chart for monthly spending trend"""
    fig = px.line(
        monthly_expenses,
        x='Month',
        y='Amount',
        markers=True,
        title="Monthly Expenses Over Time"
    )
    fig.update_traces(line_color='#1f77b4', line_width=3, marker=dict(size=8))
    fig.update_layout(height=400)
    return fig


def create_prediction_chart(monthly_data, predicted_expense):
    """Create chart showing actual vs predicted spending"""
    fig = go.Figure()
    
    # Actual spending
    fig.add_trace(go.Scatter(
        x=monthly_data['Month'],
        y=monthly_data['Amount'],
        mode='lines+markers',
        name='Actual',
        line=dict(color='blue', width=3),
        marker=dict(size=8)
    ))
    
    # Predicted spending
    fig.add_trace(go.Scatter(
        x=['Next Month'],
        y=[predicted_expense],
        mode='markers',
        name='Predicted',
        marker=dict(size=20, color='red', symbol='star')
    ))
    
    fig.update_layout(
        title='Actual vs Predicted Spending',
        xaxis_title='Month',
        yaxis_title='Amount (₹)',
        height=400
    )
    return fig


def create_day_of_week_chart(day_spending):
    """Create bar chart for day of week spending"""
    fig = px.bar(
        x=day_spending.index,
        y=day_spending.values,
        labels={'x': 'Day', 'y': 'Amount (₹)'},
        color=day_spending.values,
        color_continuous_scale='Purples'
    )
    fig.update_layout(showlegend=False, height=400)
    return fig
