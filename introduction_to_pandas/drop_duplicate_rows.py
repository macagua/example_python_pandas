"""Drop duplicate rows based on the 'email' column example."""
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicate rows based on the 'email' column

    Args:
        customers (pd.DataFrame): The DataFrame containing customer data

    Returns:
        pd.DataFrame: The DataFrame with duplicate rows removed
    """
    return customers.drop_duplicates(subset=['email'])

# Sample Data
data = {
    'customer_id': [101, 53, 128, 3, 5],
    'name': ['Leonardo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'email': ['leonardoc@example.com', 'anap@example.com', 'hectmarr@example.com', 'diegol@example.com', 'diegol@example.com'],
}

customers = pd.DataFrame(data)

# Call the function
dropDuplicateEmails(customers)
