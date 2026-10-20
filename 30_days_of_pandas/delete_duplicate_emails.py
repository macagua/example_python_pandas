"""Delete duplicate emails from the DataFrame example."""
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """Delete duplicate emails from the DataFrame.

    Args:
        person (pd.DataFrame): DataFrame containing person data.

    Returns:
        pd.DataFrame: DataFrame with duplicate emails removed.
    """
    # Sort the DataFrame by 'id' in ascending order to ensure that the first occurrence of each email is kept
    person.sort_values(by='id', inplace=True)
    # Drop duplicate emails, keeping the first occurrence of each email
    person.drop_duplicates(subset=['email'], inplace=True)

person_data = {
    'id': [1, 2, 3],
    'email': ['leonardo@example.com', 'ana@example.com', 'leonardo@example.com']
}
person = pd.DataFrame(person_data)

# Call the function
delete_duplicate_emails(person)
