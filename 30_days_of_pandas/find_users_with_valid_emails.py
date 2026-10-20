"""Get users with valid emails based on a specific regex pattern example."""
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """Get users with valid emails based on a specific regex pattern.

    Args:
        users (pd.DataFrame): dataframe containing user information with an 'email' column.

    Returns:
        pd.DataFrame: dataframe containing only users with valid emails.
    """
    # Use the str.match() method with a regex pattern to find valid emails
    users_valid_emails = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    return users_valid_emails

data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Leonardo', 'Ana', 'Yelitze', 'Miriam', 'Rafael', 'Medardo', 'Diego'],
    'mail': [
        'leonardoc@leetcode.com',
        'anacpg',
        'yelitze-m@leetcode.com',
        'miriam.yelitza@leetcode.com',
        'rafael#2022l@leetcode.com',
        'medardo45@gmail.com',
        '.diegol@leetcode.com'
    ],
}
users = pd.DataFrame(data)

# Call the function
valid_emails(users)
