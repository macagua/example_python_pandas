"""Categorize Products by Sell Date example."""
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    """Categorize Products by Sell Date

    Args:
        activities (pd.DataFrame): DataFrame containing product activities with columns 'sell_date'

    Returns:
        pd.DataFrame: DataFrame with columns 'sell_date', 'num_sold
    """    
    return activities.groupby(
        'sell_date'
    )['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()

# Sample Data
data = {
    'sell_date': [
        pd.Timestamp('2020-05-30'),
        pd.Timestamp('2020-06-01'),
        pd.Timestamp('2020-06-02'),
        pd.Timestamp('2020-05-30'),
        pd.Timestamp('2020-06-01'),
        pd.Timestamp('2020-06-02'),
        pd.Timestamp('2020-05-30')
    ],
    'product': [
        'Headphone',
        'Pencil',
        'Mask',
        'Basketball',
        'Bible',
        'Mask',
        'T-Shirt'
        ],
}
activities = pd.DataFrame(data)

# Call the function
categorize_products(activities)
