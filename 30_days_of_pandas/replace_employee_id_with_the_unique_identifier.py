"""Replace Employee ID With The Unique Identifier example."""
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employees_uni: pd.DataFrame) -> pd.DataFrame:
    """Merge the employees DataFrame with the employees_unique DataFrame on

    Args:
        employees (pd.DataFrame): DataFrame containing employee data with columns 'id'
        employees_uni (pd.DataFrame): DataFrame containing unique employee data with columns 'unique_id'

    Returns:
        pd.DataFrame: DataFrame merged DataFrame with columns 'unique_id' and 'name'
    """
    # Merge the employees DataFrame with the employees_unique DataFrame on
    df = pd.merge(
        employees, employees_uni,
        on = 'id',
        how = 'left'
    )
    # Replace the 'employee_id' column with 'unique_id' from the merged DataFrame
    return df[['unique_id', 'name']]

# Sample Datas
employees_data = {
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan'],
}
employees = pd.DataFrame(employees_data)

employees_uni_data = {
    'id': [3, 11,90],
    'unique_id': [1, 2, 3],
}
employees_uni = pd.DataFrame(employees_uni_data)

# Call the function
replace_employee_id(employees, employees_uni)
