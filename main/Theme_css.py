
import streamlit as st
# Theme configuration
def apply_theme(theme):
    if theme == "Dark":
        st.markdown("""
    <style>
    /* Limit width for all plot containers */
    .element-container:has(.stPlotlyChart),
    .element-container:has(.stImage),
    .element-container:has(.stPyplot),
    .element-container:has(.stAltairChart) {
        max-width: 700px !important;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)
        
        
        st.markdown("""
            <style>

            .stApp {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            .stMetric {
                background-color: #2D2D2D;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                color: #FFFFFF;
            }
            .stMetric h3 {
                color: #4CAF50;
            }
            .stMetric .value {
                font-size: 24px;
                font-weight: bold;
                color: #FFFFFF;
            }
            .stMetric .delta {
                font-size: 14px;
                color: #B0B0B0;
            }
            .css-1d391kg {
                padding: 1rem;
                border-radius: 0.5rem;
                background-color: #2D2D2D;
                color: #FFFFFF;
            }
            .search-box {
                padding: 8px;
                border-radius: 4px;
                border: 1px solid #404040;
                background-color: #2D2D2D;
                color: #FFFFFF;
                width: 100%;
            }
            .stTabs [data-baseweb="tab-list"] {
                background-color: #2D2D2D;
            }
            .stTabs [data-baseweb="tab"] {
                color: #FFFFFF;
            }
            .stTabs [aria-selected="true"] {
                background-color: #4CAF50;
                color: #FFFFFF;
            }
            .stMarkdown {
                color: #FFFFFF;
            }
            .stDataFrame {
                background-color: #2D2D2D;
            }
            .stPlotlyChart {
                background-color: #2D2D2D;
            }
            .visualization-container {
                margin-bottom: 2rem;
            }
            .header-container {
                text-align: center;
                padding: 2rem 1rem;
                margin-bottom: 2rem;
            }
            .main-title {
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 1rem;
                line-height: 1.2;
            }
            .gradient-text {
                background: linear-gradient(45deg, #4CAF50, #FFFFFF);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .slogan {
                font-style: italic;
                color: #B0B0B0;
                font-size: 1.1rem;
                margin-top: 0.5rem;
                opacity: 0.9;
                text-align: left;
            }
            @media (max-width: 768px) {
                .main-title {
                    font-size: 2rem;
                }
                .slogan {
                    font-size: 1rem;
                }
            }
            /* Enhanced Header Styles */
            .section-header {
                background: linear-gradient(90deg, #4CAF50 0%, #2D2D2D 100%);
                color: white;
                padding: 1.5rem;
                border-radius: 20px;
                margin: 1rem 0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
                text-align: center;
                font-size: 1.5rem;
                font-weight: bold;
                letter-spacing: 1px;
                text-transform: uppercase;
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
                overflow: hidden;
                border: 2px solid transparent;
                background-clip: padding-box;
                position: relative;
            }
            .section-header::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, rgba(76, 175, 80, 0.1), rgba(45, 45, 45, 0.1));
                z-index: 1;
                border-radius: 20px;
            }
            .section-header::after {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(45deg, #4CAF50, #2D2D2D);
                z-index: -1;
                border-radius: 22px;
            }
            .section-header:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0,0,0,0.2);
            }
            .section-subheader {
                background: linear-gradient(90deg, #2D2D2D 0%, #1E1E1E 100%);
                color: white;
                padding: 1rem;
                border-radius: 15px;
                margin: 0.5rem 0;
                border-left: 4px solid #4CAF50;
                font-size: 1.2rem;
                font-weight: 500;
                text-align: center;
                position: relative;
                overflow: hidden;
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                border: 2px solid transparent;
                background-clip: padding-box;
            }
            .section-subheader::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, rgba(45, 45, 45, 0.1), rgba(30, 30, 30, 0.1));
                z-index: 1;
                border-radius: 15px;
            }
            .section-subheader::after {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(45deg, #2D2D2D, #1E1E1E);
                z-index: -1;
                border-radius: 17px;
            }
            @media (max-width: 768px) {
                .section-header {
                    padding: 1rem;
                    font-size: 1.2rem;
                    border-radius: 15px;
                    margin: 0.5rem 0;
                }
                .section-header::after {
                    border-radius: 17px;
                }
                .section-subheader {
                    padding: 0.8rem;
                    font-size: 1rem;
                    border-radius: 12px;
                    margin: 0.3rem 0;
                }
                .section-subheader::after {
                    border-radius: 14px;
                }
            }
            /* Tab styling */
            .stTabs {
                background-color: #1E1E1E;
                border-radius: 20px;
                padding: 0.5rem;
                margin-bottom: 1rem;
            }
            .stTabs [data-baseweb="tab-list"] {
                background-color: #2D2D2D;
                border-radius: 15px;
                padding: 0.5rem;
                gap: 0;
                display: flex;
                width: 100%;
            }
            .stTabs [data-baseweb="tab"] {
                background-color: transparent;
                color: #FFFFFF;
                border: none;
                border-radius: 12px;
                padding: 1rem 2rem;
                margin: 0;
                flex: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 600;
                font-size: 1rem;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            .stTabs [data-baseweb="tab"]::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, rgba(76, 175, 80, 0.1), rgba(45, 45, 45, 0.1));
                opacity: 0;
                transition: opacity 0.3s ease;
            }
            .stTabs [data-baseweb="tab"]:hover::before {
                opacity: 1;
            }
            .stTabs [aria-selected="true"] {
                background: linear-gradient(90deg, #4CAF50 0%, #2D2D2D 100%) !important;
                color: white !important;
                border: none !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                transform: translateY(-1px);
            }
            .stTabs [aria-selected="true"]::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #4CAF50, #2D2D2D);
            }

            /* Footer styling */
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: calc(100% - var(--sidebar-width, 0px));
                background: linear-gradient(90deg, #1E1E1E 0%, #2D2D2D 100%);
                padding: 0.5rem;
                text-align: center;
                border-top: 2px solid transparent;
                background-clip: padding-box;
                z-index: 999;
                margin-left: var(--sidebar-width, 0px);
                transition: all 0.3s ease;
            }
            [data-testid="stSidebar"][aria-expanded="true"] ~ .footer {
                margin-left: var(--sidebar-width, 21rem);
                width: calc(100% - var(--sidebar-width, 21rem));
            }
            [data-testid="stSidebar"][aria-expanded="false"] ~ .footer {
                margin-left: var(--sidebar-width, 0px);
                width: calc(100% - var(--sidebar-width, 0px));
            }
            .footer-content {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 0.2rem;
                width: 100%;
            }
            .app-name {
                font-size: 1rem;
                font-weight: bold;
                background: linear-gradient(45deg, #4CAF50, #FFFFFF);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-transform: uppercase;
                letter-spacing: 1px;
                width: 100%;
                text-align: center;
            }
            .app-slogan {
                color: #B0B0B0;
                font-size: 0.75rem;
                font-style: italic;
                width: 100%;
                text-align: center;
            }
            @media (max-width: 768px) {
                .footer {
                    padding: 0.4rem;
                    width: 100%;
                    margin-left: 0;
                }
                [data-testid="stSidebar"][aria-expanded="true"] ~ .footer {
                    margin-left: 0;
                    width: 100%;
                }
                .app-name {
                    font-size: 0.9rem;
                }
                .app-slogan {
                    font-size: 0.7rem;
                }
            }
            @media (max-width: 480px) {
                .footer {
                    padding: 0.3rem;
                }
                .app-name {
                    font-size: 0.8rem;
                }
                .app-slogan {
                    font-size: 0.65rem;
                }
            }
            /* Add these styles for plot containers */
            [data-testid="stImage"], [data-testid="stPlotlyChart"] {
                background-color: transparent !important;
            }
            .element-container div[data-testid="stVerticalBlock"] {
                background-color: transparent !important;
            }
            /* Make sure pyplot output is transparent */
            .stMarkdown div[data-testid="stMarkdownContainer"] > div {
                background-color: transparent !important;
            }
            .regression-summary {
                background-color: #2D2D2D;
                padding: 1.5rem;
                border-radius: 8px;
                margin: 1rem 0;
                font-family: 'Courier New', monospace;
                white-space: pre;
                color: #FFFFFF;
                overflow-x: auto;
                line-height: 1.5;
            }
            .regression-header {
                color: #4CAF50;
                font-weight: bold;
                margin-bottom: 1rem;
                font-family: 'Courier New', monospace;
            }
            .regression-text {
                font-family: 'Courier New', monospace;
                white-space: pre;
                color: #FFFFFF;
                line-height: 1.5;
            }
            .stExpander {
                border: 1px solid #4CAF50;
                border-radius: 8px;
                margin: 1rem 0;
            }
            .stExpander .streamlit-expanderHeader {
                background: linear-gradient(90deg, #2D2D2D 0%, #1E1E1E 100%);
                color: #4CAF50;
                padding: 1.2rem;
                border-radius: 8px;
                transition: all 0.3s ease;
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                border-left: 4px solid #4CAF50;
            }
            .stExpander .streamlit-expanderHeader:hover {
                background: linear-gradient(90deg, #3D3D3D 0%, #2D2D2D 100%);
            }
            .stExpander .streamlit-expanderHeader span {
                text-align: center;
                font-weight: bold;
                letter-spacing: 0.5px;
                font-size: 1.1rem;
                text-transform: uppercase;
                background: linear-gradient(45deg, #4CAF50, #FFFFFF);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                padding-right: 1.5rem;
            }
            .stExpander .streamlit-expanderHeader::after {
                content: "▼";
                position: absolute;
                right: 1rem;
                transition: transform 0.3s ease;
                color: #4CAF50;
            }
            .stExpander .streamlit-expanderHeader[aria-expanded="true"]::after {
                transform: rotate(180deg);
            }
            .stExpander .streamlit-expanderContent {
                background-color: #2D2D2D;
                padding: 1rem;
                border-radius: 0 0 8px 8px;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .stApp {
                background-color: #FFFFFF;
                color: #000000;
            }
            .stMetric {
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .stMetric h3 {
                color: #1f77b4;
            }
            .stMetric .value {
                font-size: 24px;
                font-weight: bold;
            }
            .stMetric .delta {
                font-size: 14px;
            }
            .css-1d391kg {
                padding: 1rem;
                border-radius: 0.5rem;
                background-color: #f8f9fa;
            }
            .search-box {
                padding: 8px;
                border-radius: 4px;
                border: 1px solid #ccc;
                width: 100%;
            }
            .stTabs [data-baseweb="tab-list"] {
                background-color: #f0f2f6;
            }
            .stTabs [data-baseweb="tab"] {
                color: #000000;
            }
            .stTabs [aria-selected="true"] {
                background-color: #1f77b4;
                color: #FFFFFF;
            }
            .visualization-container {
                margin-bottom: 2rem;
            }
            .header-container {
                text-align: center;
                padding: 2rem 1rem;
                margin-bottom: 2rem;
            }
            .main-title {
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 1rem;
                line-height: 1.2;
            }
            .gradient-text {
                background: linear-gradient(45deg, #1f77b4, #000000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                padding-right: 0.5rem;
            }
            .subtitle {
                color: #666666;
                font-weight: normal;
            }
            .slogan {
                font-style: italic;
                color: #666666;
                font-size: 1.1rem;
                margin-top: 1rem;
                opacity: 0.9;
                text-align: center;
            }
            @media (max-width: 768px) {
                .main-title {
                    font-size: 2rem;
                }
                .slogan {
                    font-size: 1rem;
                }
            }
            /* Enhanced Header Styles */
            .section-header {
                background: linear-gradient(90deg, #1f77b4 0%, #f0f2f6 100%);
                color: white;
                padding: 1.5rem;
                border-radius: 20px;
                margin: 1rem 0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
                text-align: center;
                font-size: 1.5rem;
                font-weight: bold;
                letter-spacing: 1px;
                text-transform: uppercase;
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
                overflow: hidden;
                border: 2px solid transparent;
                background-clip: padding-box;
            }
            .section-header::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, rgba(31, 119, 180, 0.1), rgba(240, 242, 246, 0.1));
                z-index: 1;
                border-radius: 20px;
            }
            .section-header::after {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(45deg, #1f77b4, #f0f2f6);
                z-index: -1;
                border-radius: 22px;
            }
            .section-header:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0,0,0,0.2);
            }
            .section-subheader {
                background: linear-gradient(90deg, #f0f2f6 0%, #ffffff 100%);
                color: #1f77b4;
                padding: 1rem;
                border-radius: 15px;
                margin: 0.5rem 0;
                border-left: 4px solid #1f77b4;
                font-size: 1.2rem;
                font-weight: 500;
                text-align: center;
                position: relative;
                overflow: hidden;
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                border: 2px solid transparent;
                background-clip: padding-box;
            }
            .section-subheader::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, rgba(240, 242, 246, 0.1), rgba(255, 255, 255, 0.1));
                z-index: 1;
                border-radius: 15px;
            }
            .section-subheader::after {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(45deg, #f0f2f6, #ffffff);
                z-index: -1;
                border-radius: 17px;
            }
            @media (max-width: 768px) {
                .section-header {
                    padding: 1rem;
                    font-size: 1.2rem;
                    border-radius: 15px;
                    margin: 0.5rem 0;
                }
                .section-header::after {
                    border-radius: 17px;
                }
                .section-subheader {
                    padding: 0.8rem;
                    font-size: 1rem;
                    border-radius: 12px;
                    margin: 0.3rem 0;
                }
                .section-subheader::after {
                    border-radius: 14px;
                }
            }
            /* Tab styling */
            .stTabs {
                background-color: #FFFFFF;
                border-radius: 20px;
                padding: 0.5rem;
                margin-bottom: 1rem;
            }
            .stTabs [data-baseweb="tab-list"] {
                background-color: #f0f2f6;
                border-radius: 15px;
                padding: 0.5rem;
                gap: 0;
                display: flex;
                width: 100%;
            }
            .stTabs [data-baseweb="tab"] {
                background-color: transparent;
                color: #000000;
                border: none;
                border-radius: 12px;
                padding: 1rem 2rem;
                margin: 0;
                flex: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 600;
                font-size: 1rem;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            .stTabs [data-baseweb="tab"]::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, rgba(31, 119, 180, 0.1), rgba(240, 242, 246, 0.1));
                opacity: 0;
                transition: opacity 0.3s ease;
            }
            .stTabs [data-baseweb="tab"]:hover::before {
                opacity: 1;
            }
            .stTabs [aria-selected="true"] {
                background: linear-gradient(90deg, #1f77b4 0%, #f0f2f6 100%) !important;
                color: white !important;
                border: none !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transform: translateY(-1px);
            }
            .stTabs [aria-selected="true"]::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #1f77b4, #f0f2f6);
            }

            /* Footer styling */
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: calc(100% - var(--sidebar-width, 0px));
                background: linear-gradient(90deg, #FFFFFF 0%, #f0f2f6 100%);
                padding: 0.5rem;
                text-align: center;
                border-top: 2px solid transparent;
                background-clip: padding-box;
                z-index: 999;
                margin-left: var(--sidebar-width, 0px);
                transition: all 0.3s ease;
            }
            [data-testid="stSidebar"][aria-expanded="true"] ~ .footer {
                margin-left: var(--sidebar-width, 21rem);
                width: calc(100% - var(--sidebar-width, 21rem));
            }
            [data-testid="stSidebar"][aria-expanded="false"] ~ .footer {
                margin-left: var(--sidebar-width, 0px);
                width: calc(100% - var(--sidebar-width, 0px));
            }
            .footer-content {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 0.2rem;
                width: 100%;
            }
            .app-name {
                font-size: 1rem;
                font-weight: bold;
                background: linear-gradient(45deg, #1f77b4, #000000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-transform: uppercase;
                letter-spacing: 1px;
                width: 100%;
                text-align: center;
            }
            .app-slogan {
                color: #666666;
                font-size: 0.75rem;
                font-style: italic;
                width: 100%;
                text-align: center;
            }
            @media (max-width: 768px) {
                .footer {
                    padding: 0.4rem;
                    width: 100%;
                    margin-left: 0;
                }
                [data-testid="stSidebar"][aria-expanded="true"] ~ .footer {
                    margin-left: 0;
                    width: 100%;
                }
                .app-name {
                    font-size: 0.9rem;
                }
                .app-slogan {
                    font-size: 0.7rem;
                }
            }
            @media (max-width: 480px) {
                .footer {
                    padding: 0.3rem;
                }
                .app-name {
                    font-size: 0.8rem;
                }
                .app-slogan {
                    font-size: 0.65rem;
                }
            }
            </style>
        """, unsafe_allow_html=True)
