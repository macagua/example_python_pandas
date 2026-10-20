"""Modify the salary column by doubling its values example.""""
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """Modify the salary column by doubling its values

    Args:
        employees (pd.DataFrame): The DataFrame containing employee data

    Returns:
        pd.DataFrame: The DataFrame with the modified salary column
    """
    return employees.assign(salary=2 * employees['salary'])

# Sample Data
data = {
    'name': ['Leonaroo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'salary': [4548, 28150, 1103, 6593, 74576],
}

employees = pd.DataFrame(data)

# Call the function
modifySalaryColumn(employees)
