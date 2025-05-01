import pandas as pd
import numpy as np
from typing import Optional, Tuple, Dict, Union
from utils import parse_price, parse_marla
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

def preprocess_rental_data(
    data: Union[str, pd.DataFrame],
    save_cleaned: bool = False,
    output_path: Optional[str] = None
) -> pd.DataFrame:
    """
    Preprocess the rental dataset by cleaning and transforming the data.
    
    Args:
        data: Either a path to the input CSV file or a DataFrame
        save_cleaned: Whether to save the cleaned dataset
        output_path: Path where to save the cleaned dataset (if save_cleaned is True)
    
    Returns:
        pd.DataFrame: Cleaned and preprocessed dataset
    """
    # Load the dataset if a path is provided
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data.copy()
    
    # 1. Remove exact duplicates
    df = df.drop_duplicates()
    
    # 2. Parse 'Price' column
    df['Price'] = df['Price'].apply(parse_price)
    
    # 3. Parse 'Marla' column
    df['Marla'] = df['Marla'].apply(parse_marla)
    
    # 4. Convert 'Bedrooms' and 'Washrooms' to numeric
    df['Bedrooms'] = pd.to_numeric(df['Bedrooms'], errors='coerce')
    df['Washrooms'] = pd.to_numeric(df['Washrooms'], errors='coerce')
    
    # 5. Impute missing values using median
    numeric_columns = ['Price', 'Marla', 'Bedrooms', 'Washrooms']
    for col in numeric_columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
    
    # Save the cleaned dataset if requested
    if save_cleaned and output_path:
        df.to_csv(output_path, index=False)
    
    return df

def create_categorical_plots(df: pd.DataFrame) -> Dict[str, plt.Figure]:
    """
    Create bar charts for categorical variables (Bedrooms, Washrooms, Marla).
    
    Args:
        df: Preprocessed DataFrame containing rental data
    
    Returns:
        Dict[str, plt.Figure]: Dictionary containing the generated figures
    """
    # Bar charts for categorical counts
    fig_categorical, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Create countplots
    sns.countplot(x='Bedrooms', data=df, ax=axes[0])
    sns.countplot(x='Washrooms', data=df, ax=axes[1])
    sns.countplot(x='Marla', data=df, ax=axes[2])
    
    # Set titles
    axes[0].set_title('Distribution of Bedrooms')
    axes[1].set_title('Distribution of Washrooms')
    axes[2].set_title('Distribution of Marla')
    
    plt.tight_layout()
    
    return {"categorical_plots": fig_categorical}

def create_price_distribution_plot(df: pd.DataFrame) -> plt.Figure:
    """
    Create a histogram for price distribution.
    
    Args:
        df: Preprocessed DataFrame containing rental data
    
    Returns:
        plt.Figure: Generated histogram figure
    """
    fig_price = plt.figure(figsize=(8, 5))
    sns.histplot(df['Price'], kde=True, bins=30)
    plt.title('Rental Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Count')
    
    return fig_price

def create_boxplots(df: pd.DataFrame) -> plt.Figure:
    """
    Create boxplots for Price and Marla.
    
    Args:
        df: Preprocessed DataFrame containing rental data
    
    Returns:
        plt.Figure: Generated boxplot figure
    """
    fig_box, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.boxplot(y='Price', data=df, ax=axes[0])
    sns.boxplot(y='Marla', data=df, ax=axes[1])
    axes[0].set_title('Price Distribution (Boxplot)')
    axes[1].set_title('Marla Distribution (Boxplot)')
    
    plt.tight_layout()
    
    return fig_box

def generate_all_visualizations(df: pd.DataFrame) -> Dict[str, plt.Figure]:
    """
    Generate all visualization plots for the dataset.
    
    Args:
        df: Preprocessed DataFrame containing rental data
    
    Returns:
        Dict[str, plt.Figure]: Dictionary containing all generated figures
    """
    plots = {}
    
    # Generate all plots
    plots.update(create_categorical_plots(df))
    plots["price_distribution"] = create_price_distribution_plot(df)
    plots["boxplots"] = create_boxplots(df)
    
    return plots
