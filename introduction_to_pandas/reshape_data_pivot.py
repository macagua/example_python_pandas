"""Pivot the weather DataFrame example."""
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """Pivot the weather DataFrame

    Args:
        weather (pd.DataFrame): The DataFrame containing weather data

    Returns:
        pd.DataFrame: The pivoted DataFrame
    """
    return weather.pivot(index="month", columns="city", values="temperature")

# Sample Data
data = {
    'city': ['Madrid', 'Barcelona', 'Valencia', 'Guadalajara', 'Fuenlabrada'],
    'month': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'temperature': [13, 23, 3, 5, 34],
}

weather = pd.DataFrame(data)

# Call the function
pivotTable(weather)
