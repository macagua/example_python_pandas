"""Select the first three rows of the DataFrame example."""
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """Select the first three rows of the DataFrame

    Args:
        employees (pd.DataFrame): A DataFrame containing employee data

    Returns:
        pd.DataFrame: A DataFrame with the first three rows
    """
    return employees.head(3)

# Sample Data
data = {
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Leonaroo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'department': ['Engineering', 'Finance', 'Sales', 'Marketing', 'HR'],
    'salary': [85000, 50000, 60000, 70000, 90000]
}

employees = pd.DataFrame(data)

# Call the function
selectFirstRows(employees)
