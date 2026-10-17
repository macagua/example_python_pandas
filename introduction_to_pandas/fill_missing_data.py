"""Fill missing values in the 'quantity' column with 0"""
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values in the 'quantity' column with 0

    Args:
        products (pd.DataFrame): The DataFrame containing product data

    Returns:
        pd.DataFrame: The DataFrame with missing values filled
    """
    products["quantity"].fillna(0, inplace=True)
    return products

# Sample Data
data = {
    'name': ['Leonaroo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'quantity': [None, None, 779, 848, 376],
    'price ': [1450, 9423, 447, 3485, 7472],
}

products = pd.DataFrame(data)

# Call the function
fillMissingValues(products)
