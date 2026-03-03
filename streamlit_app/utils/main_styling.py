import streamlit as st


def load_custom_css():
    """Load custom CSS styles for the Streamlit app"""
    css = """
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global font and color styles */
    body, .stApp {
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
        color: #3c3c3c;
    }

    /* Custom button styles */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        margin: 0.5em 0;
        padding: 0.75em 1.5em;
        transition: all 0.3s ease;
        border: none;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931A 100%);
        color: white;
    }

    /* Sidebar styles */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }

    section[data-testid="stSidebar"] .stMarkdown h1 {
        color: #FF6B35;
    }

    /* Table styles */
    .dataframe tbody th, .dataframe tbody td {
        padding: 0.4em;
    }

    /* Card styles */
    .card {
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        padding: 1.5em;
        margin: 0.75em 0;
        transition: all 0.3s ease;
    }

    .card:hover {
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
        transform: translateY(-2px);
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: #1a1a2e;
    }

    /* Divider styling */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #ddd, transparent);
        margin: 2rem 0;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 16px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
