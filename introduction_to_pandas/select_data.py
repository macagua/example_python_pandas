"""Select data from a DataFrame example."""
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """Select data from a DataFrame

    Args:
        students (pd.DataFrame): The DataFrame containing student data

    Returns:
        pd.DataFrame: A DataFrame with the name and age of the student with ID 101
    """
    return students.loc[students['student_id'] == 101, ['name', 'age']]

# Sample Data
data = {
    'student_id': [101, 53, 128, 3, 5],
    'name': ['Leonaroo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'age': [45, 42, 44, 47, 46],
}

students = pd.DataFrame(data)

# Call the function
selectData(students)
