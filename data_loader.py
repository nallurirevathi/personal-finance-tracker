"""
Data loading and processing module
"""

import pandas as pd
import streamlit as st
from utils import parse_date
from config import DATA_FILE


@st.cache_data
def load_data():
    """Load and preprocess expense data"""
    # Load CSV
    df = pd.read_csv(DATA_FILE, encoding='utf-8')
    
    # Parse dates
    df['Date'] = df['Date'].apply(parse_date)
    df = df.dropna(subset=['Date'])
    
    # Extract date components
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    df['MonthName'] = df['Date'].dt.strftime('%B %Y')
    df['DayOfWeek'] = df['Date'].dt.day_name()
    df['MonthYear'] = df['Date'].dt.strftime('%Y-%m')
    
    return df


def filter_data(df, transaction_type, category, year):
    """Filter dataframe based on user selections"""
    filtered_df = df.copy()
    
    if transaction_type != 'All':
        filtered_df = filtered_df[filtered_df['Income/Expense'] == transaction_type]
    
    if category != 'All':
        filtered_df = filtered_df[filtered_df['Category'] == category]
    
    if year != 'All':
        filtered_df = filtered_df[filtered_df['Year'] == year]
    
    return filtered_df


def get_expenses_only(df):
    """Filter to get only expense transactions"""
    return df[df['Income/Expense'] == 'Expense'].copy()


def get_summary_stats(df):
    """Calculate summary statistics"""
    expense_df = df[df['Income/Expense'] == 'Expense']
    
    return {
        'total_spent': expense_df['Amount'].sum(),
        'avg_expense': expense_df['Amount'].mean(),
        'max_expense': expense_df['Amount'].max(),
        'min_expense': expense_df['Amount'].min(),
        'total_transactions': len(df),
        'unique_categories': df['Category'].nunique()
    }
