"""Counts the number of accounts in each salary category example"""
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    """Counts the number of accounts in each salary category.

    Args:
        accounts (pd.DataFrame): The input DataFrame containing account information.

    Returns:
        pd.DataFrame: A DataFrame with the count of accounts in each salary category.
    """
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            accounts[accounts.income < 20000].shape[0],
            accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
            accounts[accounts.income > 50000].shape[0],
        ],
    })

# Sample Data
data = {
    'account_id': [3, 2, 8, 6],
    'income': [108939, 12747, 87709, 91796],
}
accounts = pd.DataFrame(data)

# Call the function
count_salary_categories(accounts)
