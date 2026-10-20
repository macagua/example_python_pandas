"""Rename the columns of the DataFrame example."""
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """Rename the columns of the DataFrame

    Args:
        students (pd.DataFrame): The DataFrame containing student data

    Returns:
        pd.DataFrame: The DataFrame with renamed columns
    """
    df_renamed = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return df_renamed

# Sample Data
data = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Leonaroo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'last': ['Leonaroo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'age': [45, 42, 44, 48, 4],
}

students = pd.DataFrame(data)

# Call the function
renameColumns(students)
