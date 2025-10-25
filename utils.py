"""
Utility functions for data processing and formatting
"""

import pandas as pd
from config import DATE_FORMAT_WITH_TIME, DATE_FORMAT_WITHOUT_TIME


def parse_date(date_str):
    """Parse date string to datetime object"""
    try:
        return pd.to_datetime(date_str, format=DATE_FORMAT_WITH_TIME)
    except:
        try:
            return pd.to_datetime(date_str, format=DATE_FORMAT_WITHOUT_TIME)
        except:
            return pd.NaT


def format_currency(amount):
    """Format amount as Indian currency"""
    return f"₹{amount:,.0f}"


def format_currency_detailed(amount):
    """Format amount as Indian currency with decimals"""
    return f"₹{amount:,.2f}"


def calculate_percentage_change(current, previous):
    """Calculate percentage change between two values"""
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100
