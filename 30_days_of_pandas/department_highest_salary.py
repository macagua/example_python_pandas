"""Find the highest salary in each department example.""""
import pandas as pd

def department_highest_salary(employees: pd.DataFrame, departments: pd.DataFrame) -> pd.DataFrame:
    """Find the highest salary in each department.

    Args:
        employees (pd.DataFrame): DataFrame containing employee information.
        departments (pd.DataFrame): DataFrame containing department information.

    Returns:
        pd.DataFrame: DataFrame containing the highest salary in each department.
    """
    # Merge the employee and department DataFrames on the 'departmentId' column
    merged_df = pd.merge(employees, departments, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
    # Group by 'departmentId' and get the maximum salary for each department
    result = merged_df.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
    # Reset the index and select the relevant columns
    result_index = result.reset_index(drop=True)[['name_department', 'name_employee', 'salary']]
    # Rename the columns for clarity
    result_index.rename(columns={
        'name_department': 'Department',
        'name_employee': 'Employee',
        'salary': 'Salary'
    }, inplace=True)
    return result_index

departments_data = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}
departments = pd.DataFrame(departments_data)

employees_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Leonardo', 'Ana', 'Yelitze', 'Miriam', 'Rafael'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}
employees = pd.DataFrame(employees_data)

# Call the function
department_highest_salary(employees, departments)
