"""Calculate total time spent by each employee on each day example"""
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    """Calculate total time spent by each employee on each day

    Args:
        employees (pd.DataFrame): DataFrame containing employee data with columns 'emp_id', 'event_day', 'in_time', and 'out_time'.

    Returns:
        pd.DataFrame: DataFrame with employee IDs, event days, and total time spent on each day.
    """
    # Calculate the total time spent by each employee on each day.
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    # Group by employee ID and event day, summing the time spent, and reset the index.
    result = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()
    # Rename the columns to 'day' and 'total_time' for clarity.
    result.rename(columns={'event_day': 'day', 'time_spent': 'total_time'}, inplace=True)
    return result

# Sample Data
data = {
    'emp_id': [1, 1, 1, 2, 2],
    'event_day': [
        pd.Timestamp('2020-11-28'),
        pd.Timestamp('2020-11-28'),
        pd.Timestamp('2020-12-03'),
        pd.Timestamp('2020-11-28'),
        pd.Timestamp('2020-12-09')
    ],
    'in_time': [4, 55, 1, 3, 47],
    'out_time': [32, 200, 42, 33, 74],
}
employees = pd.DataFrame(data)

# Call the function
total_time(employees)
