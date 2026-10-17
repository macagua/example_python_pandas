"""Find the second highest salary in the employee DataFrame example"""
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """Find the second highest salary in the employee DataFrame.

    Args:
        employee (pd.DataFrame): DataFrame containing employee information.

    Returns:
        pd.DataFrame: DataFrame containing the second highest salary.
    """
    # Define the column name for the result
    col = 'SecondHighestSalary'
    # Get unique salaries in descending order
    salaries = sorted(employee['salary'].dropna().unique(), reverse=True)
    # Get the second highest salary if it exists, otherwise return pd.NA
    result = salaries[1] if len(salaries) >= 2 else pd.NA
    # Return the result as a DataFrame with the specified column name
    return pd.DataFrame({col: [result]})

data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300],
}
employee = pd.DataFrame(data)

# Call the function
second_highest_salary(employee)
