"""Find customers who have never placed an order example"""
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Find customers who have never placed an order

    Args:
        customers (pd.DataFrame): The DataFrame containing customer data
        orders (pd.DataFrame): The DataFrame containing order data

    Returns:
        pd.DataFrame: The DataFrame with customers who have never placed an order
    """
    # Merge customers and orders on the customer ID
    df = pd.merge(customers, orders, how="outer", left_on="id", right_on="customerId")
    # Fill NaN values with 0 for customerId
    df = df.fillna(0)
    # Filter customers who have never placed an order (customerId == 0)
    df = df[(df["customerId"]==0)]
    # Rename the 'name' column to 'Customers' and return only that column as a DataFrame
    df.rename(columns={"name": "Customers"}, inplace=True)
    # Return only the 'Customers' column as a DataFrame
    return df['Customers'].to_frame()

# Sample Data
data_customers = {
    'id': [0, 1, 2, 3, 4],
    'name': ['Leo', 'Ana', 'Liliana', 'Virginia', 'Maria'],
}
customers = pd.DataFrame(data_customers)

data_orders = {
    'id': [0, 1],
    'customerId': [1, 3],
}
orders = pd.DataFrame(data_orders)

# Call the function
find_customers(customers, orders)
