"""Find the Nth highest salary in the employee DataFrame example."""
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """Find the Nth highest salary in the employee DataFrame.

    Args:
        employee (pd.DataFrame): DataFrame containing employee information.
        N (int): The rank of the salary to find.

    Returns:
        pd.DataFrame: DataFrame containing the Nth highest salary.
    """
    # Define the column name for the result
    col = f'getNthHighestSalary({N})'
    # Get unique salaries in descending order and select the Nth highest salary
    salaries = sorted(employee['salary'].dropna().unique(), reverse=True)
    # Get the Nth highest salary if it exists, otherwise return pd.NA
    result = salaries[N - 1] if N <= len(salaries) and N >= 1 else pd.NA
    # Return the result as a DataFrame with the specified column name
    return pd.DataFrame({col: [result]})

data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300],
}
employee = pd.DataFrame(data)

# Call the function
nth_highest_salary(employee, N=2)
