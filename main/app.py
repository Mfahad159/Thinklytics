import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from analysis import preprocess_rental_data, generate_all_visualizations
from summary import get_market_insights
from statistical_analysis import (
    calculate_descriptive_stats,
    calculate_confidence_intervals as calculate_stats_confidence_intervals,
    analyze_distributions,
    create_qq_plot,
    perform_regression_analysis,
    create_distribution_plots,
    create_prediction_plot
)
import traceback
from pathlib import Path
import logging
import sys
import time
import random
import matplotlib.pyplot as plt
import seaborn as sns
from advanced_analysis import (
    calculate_confidence_intervals as calculate_advanced_confidence_intervals,
    analyze_distribution,
    create_distribution_plots as create_advanced_distribution_plots,
    perform_regression_analysis as perform_advanced_regression_analysis,
    create_regression_plots
)
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.stylable_container import stylable_container
import streamlit.components.v1 as components

# Set page config must be the first Streamlit command
st.set_page_config(
    page_title="ThinkLytics",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme configuration
def apply_theme(theme):
    if theme == "Dark":
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

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def create_heatmap(df, theme):
    """Create a correlation heatmap."""
    # Reduce figure size by 15%
    fig = plt.figure(figsize=(3.5, 2.3), facecolor='none')  # Set transparent background
    ax = fig.add_subplot(111)
    numeric_df = df.select_dtypes(include=[np.number])
    correlation_matrix = numeric_df.corr()
    
    if theme == "Dark":
        plt.style.use('dark_background')
        ax.set_facecolor('none')  # Transparent axis background
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', 
                   linewidths=0.5, cbar_kws={'label': 'Correlation'}, ax=ax,
                   annot_kws={'color': 'white', 'size': 8})  # Reduced annotation size
        # Set text colors for dark theme
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.tick_params(colors='white', labelsize=8)  # Reduced tick label size
        for spine in ax.spines.values():
            spine.set_color('white')
    else:
        ax.set_facecolor('none')  # Transparent axis background
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', 
                   linewidths=0.5, cbar_kws={'label': 'Correlation'}, ax=ax,
                   annot_kws={'color': 'black', 'size': 8})  # Reduced annotation size
        # Set text colors for light theme
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')
        ax.title.set_color('black')
        ax.tick_params(colors='black', labelsize=8)  # Reduced tick label size
        for spine in ax.spines.values():
            spine.set_color('black')
    
    plt.title('Correlation Heatmap of Numeric Features', pad=15, fontsize=12, fontweight='bold')  # Reduced title size
    plt.tight_layout(pad=1.5)
    
    # Set figure background to transparent
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    return fig

def format_price_pakistani(value):
    """Format price in Pakistani numbering system (lakhs, crores)."""
    if value >= 10000000:  # 1 crore
        return f"{value/10000000:.2f}Cr"
    elif value >= 100000:  # 1 lakh
        return f"{value/100000:.2f}L"
    elif value >= 1000:
        return f"{value/1000:.0f}K"
    return f"{value:.0f}"

def create_price_distribution(df, theme):
    """Create price distribution plot."""
    # Reduce figure size by additional 10%
    fig = plt.figure(figsize=(5.0, 2.5), facecolor='none')  # Set transparent background
    ax = fig.add_subplot(111)
    
    if theme == "Dark":
        plt.style.use('dark_background')
        ax.set_facecolor('none')  # Transparent axis background
        plt.hist(df['Price'], bins=30, color='#4CAF50', edgecolor='white', alpha=0.8)
        # Set text colors for dark theme
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('white')
    else:
        ax.set_facecolor('none')  # Transparent axis background
        plt.hist(df['Price'], bins=30, color='#1f77b4', edgecolor='black', alpha=0.8)
        # Set text colors for light theme
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')
        ax.title.set_color('black')
        ax.tick_params(colors='black')
        for spine in ax.spines.values():
            spine.set_color('black')
    
    plt.title('Price Distribution', pad=15, fontsize=14, fontweight='bold')
    plt.xlabel('Price', fontsize=11)
    plt.ylabel('Frequency', fontsize=11)
    plt.grid(True, alpha=0.2, color='white' if theme == "Dark" else 'black')
    
    # Format x-axis ticks in Pakistani numbering system
    current_values = ax.get_xticks()
    ax.set_xticklabels([format_price_pakistani(x) for x in current_values])
    plt.xticks(rotation=45)  # Rotate labels for better readability
    
    # Adjust layout to prevent cutoff
    plt.tight_layout(pad=1.5)
    
    # Set figure background to transparent
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    return fig

def create_regression_analysis(df, theme):
    """Create regression analysis plots."""
    # Reduce figure size by 15%
    fig = plt.figure(figsize=(3.5, 2.3), facecolor='none')  # Set transparent background
    ax = fig.add_subplot(111)
    
    if theme == "Dark":
        plt.style.use('dark_background')
        ax.set_facecolor('none')  # Transparent axis background
        sns.regplot(x='Marla', y='Price', data=df, color='#4CAF50', 
                   scatter_kws={'alpha':0.5, 's': 20}, ax=ax)  # Reduced scatter point size
        # Set text colors for dark theme
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.tick_params(colors='white', labelsize=8)  # Reduced tick label size
        for spine in ax.spines.values():
            spine.set_color('white')
    else:
        ax.set_facecolor('none')  # Transparent axis background
        sns.regplot(x='Marla', y='Price', data=df, color='#1f77b4', 
                   scatter_kws={'alpha':0.5, 's': 20}, ax=ax)  # Reduced scatter point size
        # Set text colors for light theme
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')
        ax.title.set_color('black')
        ax.tick_params(colors='black', labelsize=8)  # Reduced tick label size
        for spine in ax.spines.values():
            spine.set_color('black')
    
    plt.title('Price vs Property Size (Marla)', pad=15, fontsize=12, fontweight='bold')  # Reduced title size
    plt.xlabel('Property Size (Marla)', fontsize=9)  # Reduced label size
    plt.ylabel('Price (Rs.)', fontsize=9)  # Reduced label size
    plt.grid(True, alpha=0.2, color='white' if theme == "Dark" else 'black')
    
    # Adjust layout to prevent cutoff
    plt.tight_layout(pad=1.5)
    
    # Set figure background to transparent
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    return fig

# Error Handling Classes
class DataLoadError(Exception):
    """Exception raised for errors in loading data."""
    pass

class DataProcessingError(Exception):
    """Exception raised for errors in processing data."""
    pass

class VisualizationError(Exception):
    """Exception raised for errors in creating visualizations."""
    pass

# Performance optimization: Cache data loading and processing
@st.cache_data(ttl=3600, show_spinner=True)
def load_data():
    """Load and cache the rental data."""
    try:
        data_path = Path("data/zameen_rentals_data.csv")
        if not data_path.exists():
            raise DataLoadError("Data file not found")
        
        df = pd.read_csv(data_path)
        logger.info(f"Successfully loaded data with {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise DataLoadError(f"Failed to load data: {str(e)}")

@st.cache_data(ttl=3600, show_spinner=True)
def process_data(df):
    """Process and cache the rental data."""
    try:
        processed_df = preprocess_rental_data(df)
        logger.info("Successfully processed data")
        return processed_df
    except Exception as e:
        logger.error(f"Error processing data: {str(e)}")
        raise DataProcessingError(f"Failed to process data: {str(e)}")

def search_locations(df, search_term):
    """Search locations based on user input."""
    if not search_term:
        return sorted(df['Location'].unique())
    return sorted([loc for loc in df['Location'].unique() if search_term.lower() in loc.lower()])

def main():
    try:
        # Theme selection
        theme = "Dark"  # Set theme to Dark by default
        apply_theme(theme)
        
        # Add loading spinner
        with st.spinner("Loading data..."):
            df = load_data()
            processed_df = process_data(df)
        
        # Sidebar with filters
        st.sidebar.markdown("### Filters")
        
        # Price range filter
        min_price = int(processed_df['Price'].min())
        max_price = int(processed_df['Price'].max())
        price_range = st.sidebar.slider(
            "Price Range (Rs.)",
            min_price,
            max_price,
            (min_price, max_price)
        )
        
        # Bedrooms filter
        bedrooms = st.sidebar.multiselect(
            "Number of Bedrooms",
            options=sorted(processed_df['Bedrooms'].unique()),
            default=sorted(processed_df['Bedrooms'].unique())
        )
        
        # Location search and filter
        st.sidebar.markdown("### 🔍 Search Locations")
        search_term = st.sidebar.text_input("Type to search locations", "")
        available_locations = search_locations(processed_df, search_term)
        
        locations = st.sidebar.multiselect(
            "Select Locations",
            options=available_locations,
            default=available_locations[:10] if len(available_locations) > 10 else available_locations
        )

        # Apply filters
        filtered_df = processed_df[
            (processed_df['Price'].between(price_range[0], price_range[1])) &
            (processed_df['Bedrooms'].isin(bedrooms)) &
            (processed_df['Location'].isin(locations))
        ]
        
        # Main content
        st.markdown('<div class="header-container">', unsafe_allow_html=True)
        st.markdown('''
            <h1 class="main-title">
                <span class="gradient-text">Property Market Analysis</span>
            </h1>
            <p class="slogan" style="margin-top: -1rem;">Transforming Property Data into Intelligent Decisions</p>
            ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Key metrics with icons
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("💰 Average Price", 
                     f"Rs. {filtered_df['Price'].mean():,.0f}",
                     "Market Overview")
        with col2:
            st.metric("🏘️ Total Properties", 
                     f"{len(filtered_df):,}",
                     "Dataset Size")
        with col3:
            st.metric("📍 Top Location", 
                     filtered_df['Location'].mode()[0],
                     "Location Analysis")
        with col4:
            st.metric("🛏️ Avg. Bedrooms", 
                     f"{filtered_df['Bedrooms'].mean():.1f}",
                     "Property Features")
        
        # Tabs for different sections
        tab1, tab2, tab3, tab4 = st.tabs([
            "Trends", 
            "Standard Analysis", 
            "Insights",
            "Statistical Analysis"
        ])
        
        with tab1:
            st.markdown('<div class="section-header">Market Trends</div>', unsafe_allow_html=True)
            
            # Price Distribution
            st.markdown('<div class="section-subheader">Price Distribution</div>', unsafe_allow_html=True)
            fig_price = create_price_distribution(filtered_df, theme)
            st.pyplot(fig_price, use_container_width=True)
            
            # Location Distribution
            st.markdown('<div class="section-subheader">Location Distribution</div>', unsafe_allow_html=True)
            location_counts = filtered_df['Location'].value_counts().head(10)
            fig_location = px.bar(
                x=location_counts.index,
                y=location_counts.values,
                template='plotly_dark' if theme == "Dark" else 'plotly_white',
                width=None,
                height=None
            )
            fig_location.update_layout(
                title={
                    'text': 'Top 10 Locations by Property Count',
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': {
                        'size': 18,
                        'family': 'Arial',
                        'color': 'white' if theme == "Dark" else 'black'
                    }
                },
                margin=dict(l=50, r=50, t=80, b=50),
                autosize=True,
                font=dict(
                    size=12,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                xaxis_title="Location",
                yaxis_title="Number of Properties",
                xaxis_title_font=dict(
                    size=14,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                yaxis_title_font=dict(
                    size=14,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                showlegend=False,
                xaxis={'tickangle': -45}
            )
            st.plotly_chart(fig_location, use_container_width=True)
            
            # Price vs Bedrooms
            st.markdown('<div class="section-subheader">Price vs Bedrooms</div>', unsafe_allow_html=True)
            fig_price_bed = px.box(
                filtered_df,
                x='Bedrooms',
                y='Price',
                title='Price Distribution by Number of Bedrooms',
                template='plotly_dark' if theme == "Dark" else 'plotly_white',
                width=None,
                height=None
            )
            fig_price_bed.update_layout(
                title={
                    'text': 'Price Distribution by Number of Bedrooms',
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': {
                        'size': 18,
                        'family': 'Arial',
                        'color': 'white' if theme == "Dark" else 'black'
                    }
                },
                margin=dict(l=50, r=50, t=80, b=50),
                autosize=True,
                font=dict(
                    size=12,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                xaxis_title="Number of Bedrooms",
                yaxis_title="Price (Rs.)",
                xaxis_title_font=dict(
                    size=14,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                yaxis_title_font=dict(
                    size=14,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                showlegend=False
            )
            st.plotly_chart(fig_price_bed, use_container_width=True)
            
            # Price vs Location
            st.markdown('<div class="section-subheader">Price vs Location</div>', unsafe_allow_html=True)
            fig_price_loc = px.box(
                filtered_df,
                x='Location',
                y='Price',
                title='Price Distribution by Location',
                template='plotly_dark' if theme == "Dark" else 'plotly_white',
                width=None,
                height=None
            )
            fig_price_loc.update_layout(
                title={
                    'text': 'Price Distribution by Location',
                    'y': 0.95,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': {
                        'size': 18,
                        'family': 'Arial',
                        'color': 'white' if theme == "Dark" else 'black'
                    }
                },
                margin=dict(l=50, r=50, t=80, b=50),
                autosize=True,
                font=dict(
                    size=12,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                xaxis_title="Location",
                yaxis_title="Price (Rs.)",
                xaxis_title_font=dict(
                    size=14,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                yaxis_title_font=dict(
                    size=14,
                    family="Arial",
                    color="white" if theme == "Dark" else "black"
                ),
                xaxis={'tickangle': -45},
                showlegend=False
            )
            st.plotly_chart(fig_price_loc, use_container_width=True)
            
        with tab2:
            st.markdown('<div class="section-header">Analysis</div>', unsafe_allow_html=True)
            
            # Heatmap
            st.markdown('<div class="section-subheader">Feature Correlation Heatmap</div>', unsafe_allow_html=True)
            with st.container():
                heatmap = create_heatmap(filtered_df, theme)
                st.pyplot(heatmap, use_container_width=True)
            
            # Regression Analysis
            st.markdown('<div class="section-subheader">Regression Analysis</div>', unsafe_allow_html=True)
            with st.container():
                reg_plot = create_regression_analysis(filtered_df, theme)
                st.pyplot(reg_plot, use_container_width=True)
            
        with tab3:
            st.markdown('<div class="section-header">Market Insights</div>', unsafe_allow_html=True)
            
            # Generate market insights
            insights = get_market_insights(filtered_df)
            
            # Summary Section
            st.markdown('<div class="section-subheader">Market Summary</div>', unsafe_allow_html=True)
            with st.container():
                st.write(insights["summary"])
            
            # Predictions Section
            st.markdown('<div class="section-subheader">Market Predictions</div>', unsafe_allow_html=True)
            with st.container():
                st.write(insights["predictions"])
            
            # Key Metrics
            st.markdown('<div class="section-subheader">Key Market Metrics</div>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Average Price",
                    f"Rs. {filtered_df['Price'].mean():,.0f}",
                    f"Range: Rs. {filtered_df['Price'].min():,.0f} - Rs. {filtered_df['Price'].max():,.0f}"
                )
            
            with col2:
                st.metric(
                    "Property Size",
                    f"{filtered_df['Marla'].mean():.1f} Marla",
                    f"Range: {filtered_df['Marla'].min():.1f} - {filtered_df['Marla'].max():.1f} Marla"
                )
            
            with col3:
                st.metric(
                    "Market Size",
                    f"{len(filtered_df):,} Properties",
                    f"Across {len(filtered_df['Location'].unique())} Locations"
                )
              # Overall Summary Section (Add this first)
            st.markdown('<div class="section-subheader">Overall Summary</div>', unsafe_allow_html=True)
            with st.container():
                st.markdown(insights["overall_summary"], unsafe_allow_html=True)
            
        with tab4:
            st.markdown('<div class="section-header">Statistical Analysis</div>', unsafe_allow_html=True)
            
            # Descriptive Statistics
            st.markdown('<div class="section-subheader">Descriptive Statistics</div>', unsafe_allow_html=True)
            desc_stats = calculate_descriptive_stats(filtered_df)
            st.dataframe(desc_stats.style.format("{:.2f}"))
            
            # Confidence Intervals
            st.markdown('<div class="section-subheader">Confidence Intervals (95%)</div>', unsafe_allow_html=True)
            conf_intervals = calculate_stats_confidence_intervals(filtered_df)
            conf_df = pd.DataFrame(conf_intervals).T
            conf_df.columns = ['Lower Bound', 'Upper Bound']
            st.dataframe(conf_df.style.format("{:.2f}"))
            
            # Distribution Analysis
            st.markdown('<div class="section-subheader">Distribution Analysis</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("Price Distribution Analysis")
                price_dist = analyze_distributions(filtered_df, 'Price')
                st.write(f"Mean: {price_dist['mean']:.2f}")
                st.write(f"Standard Deviation: {price_dist['std']:.2f}")
                st.write("Shapiro-Wilk Test:")
                st.write(f"Statistic: {price_dist['shapiro_test']['statistic']:.4f}")
                st.write(f"P-value: {price_dist['shapiro_test']['p_value']:.4f}")
                
                # QQ Plot
                st.pyplot(create_qq_plot(filtered_df, 'Price', theme))
            
            with col2:
                st.write("Marla Distribution Analysis")
                marla_dist = analyze_distributions(filtered_df, 'Marla')
                st.write(f"Mean: {marla_dist['mean']:.2f}")
                st.write(f"Standard Deviation: {marla_dist['std']:.2f}")
                st.write("Shapiro-Wilk Test:")
                st.write(f"Statistic: {marla_dist['shapiro_test']['statistic']:.4f}")
                st.write(f"P-value: {marla_dist['shapiro_test']['p_value']:.4f}")
                
                # QQ Plot
                st.pyplot(create_qq_plot(filtered_df, 'Marla', theme))
            
            # Distribution Plots
            st.markdown('<div class="section-subheader">Distribution Plots with Normal Fit</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            
            with col1:
                st.pyplot(create_distribution_plots(filtered_df, 'Price', theme))
            
            with col2:
                st.pyplot(create_distribution_plots(filtered_df, 'Marla', theme))
            
            # Regression Analysis
            st.markdown('<div class="section-subheader">Multiple Regression Analysis</div>', unsafe_allow_html=True)
            
            # Feature selection for regression
            features = st.multiselect(
                "Select Features for Regression",
                options=['Marla', 'Bedrooms'],
                default=['Marla', 'Bedrooms']
            )
            
            if features:
                regression_results = perform_regression_analysis(
                    filtered_df, 
                    target='Price', 
                    features=features
                )
                
                # Display regression summary
                st.markdown("""
                    <style>
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
                    </style>
                """, unsafe_allow_html=True)

                # Display formatted results
                st.markdown('<div class="regression-summary">', unsafe_allow_html=True)
                
                # Header
                st.markdown('<div class="section-subheader">OLS Regression Results</div>', unsafe_allow_html=True)
                
                # Display the full regression summary with proper formatting
                summary_text = regression_results["model_summary"]
                # Replace multiple spaces with single space for better formatting
                summary_text = '\n'.join(' '.join(line.split()) for line in summary_text.split('\n'))
                st.markdown(f'<div class="regression-text">{summary_text}</div>', unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Prediction Plots
                st.markdown('<div class="section-subheader">Prediction Plots</div>', unsafe_allow_html=True)
                for feature in features:
                    st.pyplot(create_prediction_plot(filtered_df, 'Price', feature, theme))
            
        # Add footer at the end of your main() function
        st.markdown("""
            <div class="footer">
                <div class="footer-content">
                    <div class="app-name" style="text-align: center; width: 100%;">ThinkLytics</div>
                    <div class="app-slogan" style="text-align: center; width: 100%;">Transforming Property Data into Intelligent Decisions</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        logger.error(f"Application error: {str(e)}\n{traceback.format_exc()}")

if __name__ == "__main__":
    main() 