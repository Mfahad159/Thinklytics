import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Tuple, List

def calculate_descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate comprehensive descriptive statistics."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    stats_dict = {
        'Mean': df[numeric_cols].mean(),
        'Median': df[numeric_cols].median(),
        'Std Dev': df[numeric_cols].std(),
        'Min': df[numeric_cols].min(),
        'Max': df[numeric_cols].max(),
        'Q1': df[numeric_cols].quantile(0.25),
        'Q3': df[numeric_cols].quantile(0.75),
        'Skewness': df[numeric_cols].skew(),
        'Kurtosis': df[numeric_cols].kurtosis()
    }
    return pd.DataFrame(stats_dict)

def calculate_confidence_intervals(df: pd.DataFrame, confidence_level: float = 0.95) -> Dict[str, Tuple[float, float]]:
    """Calculate confidence intervals for numeric columns."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    intervals = {}
    
    for col in numeric_cols:
        data = df[col].dropna()
        mean = np.mean(data)
        std = np.std(data, ddof=1)
        n = len(data)
        
        # Calculate the margin of error
        margin = stats.t.ppf((1 + confidence_level) / 2, n-1) * (std / np.sqrt(n))
        
        intervals[col] = (mean - margin, mean + margin)
    
    return intervals

def analyze_distributions(df: pd.DataFrame, column: str) -> Dict:
    """Analyze distribution of a numeric column."""
    data = df[column].dropna()
    
    # Fit normal distribution
    mu, std = stats.norm.fit(data)
    
    # Perform normality tests
    shapiro_test = stats.shapiro(data)
    ks_test = stats.kstest(data, 'norm', args=(mu, std))
    
    return {
        'mean': mu,
        'std': std,
        'shapiro_test': {
            'statistic': shapiro_test.statistic,
            'p_value': shapiro_test.pvalue
        },
        'ks_test': {
            'statistic': ks_test.statistic,
            'p_value': ks_test.pvalue
        }
    }

def create_qq_plot(df: pd.DataFrame, column: str, theme: str) -> plt.Figure:
    """Create QQ plot for normality testing."""
    # Reduce figure size by 10%
    fig = plt.figure(figsize=(9, 5.4), facecolor='none')  # Set transparent background
    ax = fig.add_subplot(111)
    
    if theme == "Dark":
        plt.style.use('dark_background')
        ax.set_facecolor('none')  # Transparent axis background
        # Set text colors for dark theme
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('white')
    else:
        ax.set_facecolor('none')  # Transparent axis background
        # Set text colors for light theme
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')
        ax.title.set_color('black')
        ax.tick_params(colors='black')
        for spine in ax.spines.values():
            spine.set_color('black')
    
    stats.probplot(df[column].dropna(), dist="norm", plot=plt)
    plt.title(f'Q-Q Plot for {column}', pad=15, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.2, color='white' if theme == "Dark" else 'black')
    
    # Adjust layout to prevent cutoff
    plt.tight_layout(pad=1.5)
    
    # Set figure background to transparent
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    return fig

def perform_regression_analysis(df: pd.DataFrame, target: str, features: List[str]) -> Dict:
    """Perform multiple regression analysis."""
    # Prepare data
    X = df[features]
    y = df[target]
    
    # Add constant for intercept
    X = sm.add_constant(X)
    
    # Fit model
    model = sm.OLS(y, X).fit()
    
    # Calculate predictions and intervals
    predictions = model.get_prediction(X)
    pred_intervals = predictions.conf_int(alpha=0.05)
    
    return {
        'model_summary': model.summary().as_text(),
        'r_squared': model.rsquared,
        'adj_r_squared': model.rsquared_adj,
        'f_statistic': model.fvalue,
        'f_p_value': model.f_pvalue,
        'coefficients': model.params.to_dict(),
        'p_values': model.pvalues.to_dict(),
        'confidence_intervals': model.conf_int().to_dict(),
        'predictions': {
            'fitted_values': model.fittedvalues.tolist(),
            'prediction_intervals': pred_intervals.tolist()
        }
    }

def create_distribution_plots(df: pd.DataFrame, column: str, theme: str) -> plt.Figure:
    """Create distribution plots with fitted normal curve."""
    # Reduce figure size by 10%
    fig = plt.figure(figsize=(10.8, 5.4), facecolor='none')  # Set transparent background
    ax = fig.add_subplot(111)
    
    if theme == "Dark":
        plt.style.use('dark_background')
        ax.set_facecolor('none')  # Transparent axis background
        # Set text colors for dark theme
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('white')
    else:
        ax.set_facecolor('none')  # Transparent axis background
        # Set text colors for light theme
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')
        ax.title.set_color('black')
        ax.tick_params(colors='black')
        for spine in ax.spines.values():
            spine.set_color('black')
    
    # Histogram
    sns.histplot(data=df, x=column, kde=True, color='#4CAF50' if theme == "Dark" else '#1f77b4', 
                alpha=0.8, ax=ax)
    
    # Fit normal distribution
    mu, std = stats.norm.fit(df[column].dropna())
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    plt.plot(x, p * len(df) * (xmax - xmin) / 30, 'r', linewidth=2)
    
    plt.title(f'Distribution of {column} with Normal Fit', pad=15, fontsize=14, fontweight='bold')
    plt.xlabel(column, fontsize=11)
    plt.ylabel('Frequency', fontsize=11)
    plt.grid(True, alpha=0.2, color='white' if theme == "Dark" else 'black')
    
    # Adjust layout to prevent cutoff
    plt.tight_layout(pad=1.5)
    
    # Set figure background to transparent
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    return fig

def create_prediction_plot(df: pd.DataFrame, target: str, feature: str, theme: str) -> plt.Figure:
    """Create regression plot with prediction intervals."""
    # Reduce figure size by 10%
    fig = plt.figure(figsize=(10.8, 5.4), facecolor='none')  # Set transparent background
    ax = fig.add_subplot(111)
    
    if theme == "Dark":
        plt.style.use('dark_background')
        ax.set_facecolor('none')  # Transparent axis background
        # Set text colors for dark theme
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.tick_params(colors='white')
        for spine in ax.spines.values():
            spine.set_color('white')
    else:
        ax.set_facecolor('none')  # Transparent axis background
        # Set text colors for light theme
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')
        ax.title.set_color('black')
        ax.tick_params(colors='black')
        for spine in ax.spines.values():
            spine.set_color('black')
    
    # Fit regression
    X = sm.add_constant(df[feature])
    model = sm.OLS(df[target], X).fit()
    
    # Create prediction intervals
    pred = model.get_prediction(X)
    pred_intervals = pred.conf_int(alpha=0.05)
    
    # Plot
    plt.scatter(df[feature], df[target], alpha=0.5, color='#4CAF50' if theme == "Dark" else '#1f77b4')
    plt.plot(df[feature], model.fittedvalues, 'r-', label='Regression Line')
    plt.fill_between(df[feature], pred_intervals[:, 0], pred_intervals[:, 1], 
                    color='gray', alpha=0.2, label='95% Prediction Interval')
    
    plt.title(f'{target} vs {feature} with Prediction Intervals', pad=15, fontsize=14, fontweight='bold')
    plt.xlabel(feature, fontsize=11)
    plt.ylabel(target, fontsize=11)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.2, color='white' if theme == "Dark" else 'black')
    
    # Adjust layout to prevent cutoff
    plt.tight_layout(pad=1.5)
    
    # Set figure background to transparent
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    return fig 