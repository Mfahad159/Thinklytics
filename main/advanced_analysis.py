import pandas as pd
import numpy as np
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, Tuple

def calculate_confidence_intervals(df: pd.DataFrame, column: str, confidence_level: float = 0.95) -> Dict:
    """
    Calculate confidence intervals for a given column.
    
    Args:
        df: DataFrame containing the data
        column: Column name to analyze
        confidence_level: Confidence level (default: 0.95)
    
    Returns:
        Dict containing mean, std, and confidence intervals
    """
    data = df[column].dropna()
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    n = len(data)
    
    # Calculate standard error
    se = std / np.sqrt(n)
    
    # Calculate margin of error
    margin = stats.t.ppf((1 + confidence_level) / 2, n-1) * se
    
    return {
        'mean': mean,
        'std': std,
        'lower_ci': mean - margin,
        'upper_ci': mean + margin,
        'margin': margin
    }

def analyze_distribution(df: pd.DataFrame, column: str) -> Dict:
    """
    Analyze the probability distribution of a column.
    
    Args:
        df: DataFrame containing the data
        column: Column name to analyze
    
    Returns:
        Dict containing distribution statistics
    """
    data = df[column].dropna()
    
    # Calculate basic statistics
    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data)
    skewness = stats.skew(data)
    kurtosis = stats.kurtosis(data)
    
    # Fit normal distribution
    params = stats.norm.fit(data)
    
    return {
        'mean': mean,
        'median': median,
        'std': std,
        'skewness': skewness,
        'kurtosis': kurtosis,
        'norm_params': params
    }

def create_distribution_plots(df: pd.DataFrame, column: str) -> Dict[str, go.Figure]:
    """
    Create probability distribution plots.
    
    Args:
        df: DataFrame containing the data
        column: Column name to analyze
    
    Returns:
        Dict containing distribution plots
    """
    data = df[column].dropna()
    
    # Create histogram with KDE
    fig_hist = px.histogram(
        df, 
        x=column,
        nbins=30,
        marginal='box',
        title=f'Distribution of {column}'
    )
    
    # Add normal distribution overlay
    x_range = np.linspace(data.min(), data.max(), 100)
    params = stats.norm.fit(data)
    pdf = stats.norm.pdf(x_range, *params)
    
    fig_hist.add_trace(
        go.Scatter(
            x=x_range,
            y=pdf * len(data) * (data.max() - data.min()) / 30,
            mode='lines',
            name='Normal Distribution',
            line=dict(color='red')
        )
    )
    
    # Create CDF plot
    fig_cdf = go.Figure()
    fig_cdf.add_trace(
        go.Scatter(
            x=np.sort(data),
            y=np.arange(1, len(data)+1) / len(data),
            mode='lines',
            name='Empirical CDF'
        )
    )
    
    # Add theoretical CDF
    fig_cdf.add_trace(
        go.Scatter(
            x=x_range,
            y=stats.norm.cdf(x_range, *params),
            mode='lines',
            name='Theoretical CDF',
            line=dict(color='red')
        )
    )
    
    fig_cdf.update_layout(
        title=f'Cumulative Distribution Function of {column}',
        xaxis_title=column,
        yaxis_title='Cumulative Probability'
    )
    
    return {
        'histogram': fig_hist,
        'cdf': fig_cdf
    }

def perform_regression_analysis(df: pd.DataFrame, target: str, features: list) -> Dict:
    """
    Perform multiple regression analysis.
    
    Args:
        df: DataFrame containing the data
        target: Target variable name
        features: List of feature names
    
    Returns:
        Dict containing regression results
    """
    # Prepare data
    X = df[features]
    y = df[target]
    
    # Fit model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make predictions
    y_pred = model.predict(X)
    
    # Calculate metrics
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    
    # Calculate prediction intervals
    n = len(y)
    p = len(features)
    dof = n - p - 1
    t_value = stats.t.ppf(0.975, dof)
    
    # Calculate standard error of prediction
    residuals = y - y_pred
    residual_std = np.std(residuals)
    pred_std = residual_std * np.sqrt(1 + 1/n + (X - X.mean())**2 / ((X - X.mean())**2).sum())
    
    # Calculate prediction intervals
    lower_bound = y_pred - t_value * pred_std
    upper_bound = y_pred + t_value * pred_std
    
    return {
        'coefficients': dict(zip(features, model.coef_)),
        'intercept': model.intercept_,
        'mse': mse,
        'r2': r2,
        'prediction_intervals': {
            'lower': lower_bound,
            'upper': upper_bound
        }
    }

def create_regression_plots(df: pd.DataFrame, target: str, features: list) -> Dict[str, go.Figure]:
    """
    Create regression analysis plots.
    
    Args:
        df: DataFrame containing the data
        target: Target variable name
        features: List of feature names
    
    Returns:
        Dict containing regression plots
    """
    plots = {}
    
    # Create scatter plots with regression lines for each feature
    for feature in features:
        fig = px.scatter(
            df,
            x=feature,
            y=target,
            trendline='ols',
            title=f'{target} vs {feature}'
        )
        plots[f'{feature}_scatter'] = fig
    
    # Create residual plot
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    residuals = y - y_pred
    
    fig_residuals = px.scatter(
        x=y_pred,
        y=residuals,
        title='Residual Plot',
        labels={'x': 'Predicted Values', 'y': 'Residuals'}
    )
    fig_residuals.add_hline(y=0, line_dash='dash', line_color='red')
    plots['residuals'] = fig_residuals
    
    return plots 