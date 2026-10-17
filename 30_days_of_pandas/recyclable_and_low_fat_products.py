"""Find recyclable and low-fat products in the DataFrame example"""
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """Find recyclable and low-fat products in the DataFrame

    Args:
        products (pd.DataFrame): The DataFrame containing product data

    Returns:
        pd.DataFrame: The DataFrame with recyclable and low-fat products
    """
    return products[
        (products['low_fats'] == "Y") & \
        (products['recyclable'] == "Y")
    ][['product_id']]

# Sample Data
data = {
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable': ['N', 'Y', 'Y', 'Y', 'N'],
}
products = pd.DataFrame(data)

# Call the function
find_products(products)
