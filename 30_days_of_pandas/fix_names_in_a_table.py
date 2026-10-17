"""Fix the names in the users DataFrame to have proper capitalization example"""
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    """Fix the names in the users DataFrame to have proper capitalization.

    Args:
        users (pd.DataFrame): DataFrame containing user data.

    Returns:
        pd.DataFrame: DataFrame with fixed names.
    """
    users['name']=users['name'].apply(lambda x: x.capitalize())
    users = users.sort_values(by='user_id')
    return users

data = {
    'user_id': [1, 2, 3, 4],
    'name': ['leOnardo', 'anA pOleO', 'DIEgo', 'rafAEL'],
}
users = pd.DataFrame(data)

# Call the function
fix_names(users)
