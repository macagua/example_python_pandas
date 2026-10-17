"""Drop rows with missing data in the 'name' column example"""
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """Drop rows with missing data in the 'name' column

    Args:
        students (pd.DataFrame): The DataFrame containing student data

    Returns:
        pd.DataFrame: The DataFrame with rows containing missing data in the 'name' column removed
    """
    df_cleaned = students.dropna(subset=['name'])
    return df_cleaned

# Sample Data
data = {
    'student_id': [101, 53, 128, 3, 5],
    'name': ['Leonardo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'age': [45, 43, 44, 48, 47],
}

students = pd.DataFrame(data)

# Call the function
dropMissingData(students)
