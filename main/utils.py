import pandas as pd
import numpy as np
import re
from typing import Union, Optional

def parse_price(price_str: Union[str, float]) -> float:
    """
    Convert price strings with 'Lakh', 'Thousand', or 'Crore' to numeric values.
    
    Args:
        price_str: Price string to parse (e.g., "75 Thousand", "2.5 Lakh")
    
    Returns:
        float: Converted price value
    """
    price_str = str(price_str).lower().strip()
    if 'lakh' in price_str:
        return float(re.sub(r'[^\d.]', '', price_str)) * 100000
    elif 'thousand' in price_str:
        return float(re.sub(r'[^\d.]', '', price_str)) * 1000
    elif 'crore' in price_str:
        return float(re.sub(r'[^\d.]', '', price_str)) * 10000000
    else:
        try:
            return float(re.sub(r'[^\d.]', '', price_str))
        except:
            return np.nan

def parse_marla(marla_str: Union[str, float]) -> float:
    """
    Convert area strings with 'Kanal' or 'Marla' to numeric Marla values.
    
    Args:
        marla_str: Area string to parse (e.g., "1 Kanal", "5 Marla")
    
    Returns:
        float: Converted area value in Marla
    """
    marla_str = str(marla_str).lower().strip()
    if 'kanal' in marla_str:
        return float(re.sub(r'[^\d.]', '', marla_str)) * 20
    elif 'marla' in marla_str:
        return float(re.sub(r'[^\d.]', '', marla_str))
    else:
        try:
            return float(re.sub(r'[^\d.]', '', marla_str))
        except:
            return np.nan
