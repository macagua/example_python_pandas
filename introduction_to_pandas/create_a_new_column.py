"""Create a new column in the DataFrame example."""
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """Create a new column in the DataFrame

    Args:
        employees (pd.DataFrame): The DataFrame containing employee data

    Returns:
        pd.DataFrame: The DataFrame with the new bonus column
    """
    employees['bonus'] = employees['salary'].apply(lambda x: x * 2)
    return employees

# Sample Data
data = {
    'name': ['Leonaroo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'salary': [4548, 28150, 1103, 6593, 74576],
}

employees = pd.DataFrame(data)

# Call the function
createBonusColumn(employees)
