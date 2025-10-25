"""
Configuration file for Personal Finance Tracker
Modify settings and constants here
"""

# Page Configuration
PAGE_TITLE = "Personal Finance Tracker"
PAGE_ICON = "💰"
LAYOUT = "wide"

# Color Scheme
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'success': '#2ca02c',
    'danger': '#d62728',
    'info': '#9467bd'
}

# Chart Colors
CHART_COLORS = [
    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
    '#FF9F40', '#FF6384', '#C9CBCF', '#4BC0C0', '#FF6384'
]

# Data Settings
DATA_FILE = 'expenses.csv'
DATE_FORMAT_WITH_TIME = '%d/%m/%Y %H:%M:%S'
DATE_FORMAT_WITHOUT_TIME = '%d/%m/%Y'

# Display Settings
TOP_CATEGORIES = 10
RECENT_TRANSACTIONS = 20
TOP_EXPENSES = 10

# Days of Week Order
DAYS_ORDER = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Custom CSS
CUSTOM_CSS = """
<style>
    .main-header {
        font-size: 5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .footer {
        text-align: center;
        color: #666;
        padding: 1rem;
    }
</style>
"""
