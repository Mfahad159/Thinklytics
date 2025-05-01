# ThinkLytics - Property Market Analysis

A comprehensive data analysis and visualization tool for real estate market insights, built with Python and Streamlit.

## Features

- **Interactive Data Visualization**: Dynamic charts and graphs for market trends
- **Statistical Analysis**: Detailed statistical insights including regression analysis
- **Market Insights**: Automated market analysis and predictions
- **Advanced Filtering**: Multi-parameter filtering system for data exploration
- **Dark/Light Theme**: Responsive UI with theme support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/thinklytics.git
cd thinklytics
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
project_root/
├── main/
│   ├── analysis.py      # Statistical analysis functions
│   ├── utils.py         # Utility functions
│   └── app.py          # Main Streamlit application
├── data/
│   └── zameen_rentals_data.csv  # Dataset
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
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

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data source: Zameen.com
- Built with Streamlit
- Statistical analysis powered by SciPy and Statsmodels
