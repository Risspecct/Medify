import streamlit as st


def inject_custom_css():
    st.markdown("""
        <style>
        /* Hide Streamlit Branding & Menus */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Modern App Background & Typography */
        .stApp {
            background-color: #f8fafc;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Adjust top padding */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
            max-width: 1200px;
        }

        /* Classy Buttons */
        .stButton > button {
            background-color: #0f766e;
            color: #ffffff;
            border-radius: 8px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        .stButton > button:hover {
            background-color: #0d9488;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            transform: translateY(-1px);
            color: white;
            border: none;
        }

        /* Outline Buttons for secondary actions */
        .stButton > button[kind="secondary"] {
            background-color: transparent;
            color: #0f766e;
            border: 2px solid #0f766e;
            box-shadow: none;
        }
        .stButton > button[kind="secondary"]:hover {
            background-color: #f0fdfa;
            color: #0f766e;
            border: 2px solid #0d9488;
        }

        /* Cards & Containers */
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            border: 1px solid #e2e8f0;
        }

        /* Metric styling */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem;
            font-weight: 700;
            color: #0f766e;
        }
        [data-testid="stMetricLabel"] {
            font-size: 1rem;
            color: #64748b;
            font-weight: 500;
        }

        /* Expander styling */
        .streamlit-expanderHeader {
            background-color: #f8fafc;
            border-radius: 8px;
            font-weight: 600;
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #0f172a;
            font-weight: 700;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #e2e8f0;
        }
        
        /* Progress bar color */
        .stProgress > div > div > div > div {
            background-color: #0f766e;
        }
        
        /* Pill Tags */
        .entity-pill {
            display: inline-block;
            background-color: #e0f2fe;
            color: #0369a1;
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 600;
            margin: 4px;
            border: 1px solid #bae6fd;
        }
        </style>
    """, unsafe_allow_html=True)


def render_pill(text):
    return f'<span class="entity-pill">{text}</span>'