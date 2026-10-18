"""Rearranges the products table by melting it to have a single column for store prices example."""
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    """Rearranges the products table by melting it to have a single column for store prices.

    Args:
        products (pd.DataFrame): The input DataFrame containing product information.

    Returns:
        pd.DataFrame: The rearranged DataFrame with store prices in a single column.
    """
    # Melt the DataFrame to have a single column for store prices, with 'store'
    # as the variable name and 'price' as the value name
    return products.melt(
        id_vars = ['product_id'],
        value_vars = ['store1', 'store2', 'store3'],
        var_name = 'store',
        value_name = 'price'
    ).dropna()

products_data = {
    'product_id': [1, 2],
    'store1': [95, 70],
    'store2': [100, None],
    'store3': [105, 80]
}
products = pd.DataFrame(products_data)

# Call the function
rearrange_products_table(products)
