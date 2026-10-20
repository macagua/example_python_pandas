"""Melt the report DataFrame example."""
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """Melt the report DataFrame

    Args:
        report (pd.DataFrame): The DataFrame containing report data

    Returns:
        pd.DataFrame: The melted DataFrame
    """
    return report.melt(id_vars="product",var_name="quarter",value_name="sales")

# Sample Data
data = {
    "product": ["Umbrella", "SleepingBag"],
    "quarter_1": [417, 224],
    "quarter_2": [224, 936],
    "quarter_3": [379, 93],
    "quarter_4": [611, 875]
}

report = pd.DataFrame(data)

# Call the function
meltTable(report)
