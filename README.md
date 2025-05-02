# ThinkLytics - Property Market Analysis

A comprehensive data analysis and visualization tool for real estate market insights, built with Python and Streamlit.

## Features

- **Interactive Data Visualization**: Dynamic charts and graphs for market trends
- **Statistical Analysis**: Detailed statistical insights including regression analysis
- **Market Insights**: Automated market analysis and predictions
- **Advanced Filtering**: Multi-parameter filtering system for data exploration
- **Personalized Rent Prediction**: Instantly see your most likely monthly rent based on property size (Marla), bedrooms, and location, using a data-driven model.  
  _Look for the "Your Most Likely Monthly Rent" section in the dashboard!_
- **Dark Theme**: Responsive UI with theme support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mfahad159/Thinklytics.git
cd Thinklytics
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
Thinklytics/
├── main/
│   ├── analysis.py      # Statistical analysis functions
│   ├── utils.py         # Utility functions
│   ├── app.py          # Main Streamlit application
│   ├── summary.py      # Market insights and predictions
│   └── statistical_analysis.py  # Advanced statistical methods
├── data/
│   └── zameen_rentals_data.csv  # Dataset
├── requirements.txt     # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
```

## Usage

1. Ensure you have the dataset in the correct location (`data/zameen_rentals_data.csv`)
2. Run the Streamlit application:
```bash
streamlit run main/app.py
```

## Features in Detail

### Market Trends
- Price distribution analysis
- Location-based property distribution
- Bedroom count analysis
- Price trends across locations

### Advanced Analysis
- Correlation heatmaps
- Regression analysis
- Feature importance visualization

### Market Insights
- Automated market summaries
- Price predictions
- Key market metrics

### Statistical Analysis
- Descriptive statistics
- Confidence intervals
- Distribution analysis
- Multiple regression modeling

### Personalized Rent Prediction
- Get an instant, data-driven estimate of your most likely monthly rent
- Adjust Marla, bedrooms, and location filters to see updated predictions
- Interactive, collapsible section with themed styling for clarity and focus

## Dependencies

- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Plotly
- Seaborn
- Matplotlib
- SciPy
- Statsmodels

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- Data source: Zameen.com
- Built with Streamlit
- Statistical analysis powered by SciPy and Statsmodels

## Contributors

- [Nawal-Akhlaq](https://github.com/Nawal-Akhlaq)
