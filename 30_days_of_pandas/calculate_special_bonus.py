"""Calculate special bonus for employees based on certain conditions example."""
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    """Calculate special bonus for employees based on certain conditions.

    Args:
        employees (pd.DataFrame): DataFrame containing employee data.

    Returns:
        pd.DataFrame: DataFrame with employee IDs and their corresponding bonuses.
    """
    # check for the basic two condition
    condition = (employees['employee_id']%2!=0) & (~employees['name'].str.startswith('M'))
    # check which salary are consistent with the above condition, if not then assign bonus to 0
    employees['bonus'] = employees['salary'].where(condition, 0)
    # sort based on employee_id
    result = employees[['employee_id','bonus']].sort_values(by='employee_id')
    return result

# Sample Data
data = {
    'employee_id': [2, 3, 7, 8, 9],
    'name': ['Leonardo', 'Ana', 'Irma', 'Manuel', 'Miriam'],
    'salary': [3000, 3800, 7400, 6100, 7700],
}
employees = pd.DataFrame(data)

# Call the function
calculate_special_bonus(employees)
