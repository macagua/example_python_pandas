"""Find the customer placing the largest number of orders example"""
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """Find the customer placing the largest number of orders.

    Args:
        orders (pd.DataFrame): DataFrame containing order information.

    Returns:
        pd.DataFrame: DataFrame with the customer number of the customer placing the largest number of orders.
    """
    # Find the customer placing the largest number of orders.
    orders_grouped = orders.groupby('customer_number')[
        'order_number'
    ].count().reset_index().sort_values(
        by='order_number',
        ascending=False
    ).head(1)
    # Remove the 'order_number' column from the result to return only the customer number.
    orders_grouped.pop('order_number')
    return orders_grouped

# Sample Data
orders_data = {
    'order_number': [1, 2, 3, 4],
    'customer_number': [1, 2, 3, 3],
}
orders = pd.DataFrame(orders_data)

# Call the function
largest_orders(orders)
