"""Change the data type of the 'grade' column to integer example."""
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """Change the data type of the 'grade' column to integer

    Args:
        students (pd.DataFrame): The DataFrame containing student data

    Returns:
        pd.DataFrame: The DataFrame with the 'grade' column converted to integer
    """
    return students.astype({'grade': int})

# Sample Data
data = {
    'student_id': [1, 2, 3, 4, 5],
    'name': ['Leonaroo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'age': [45, 42, 44, 48, 4],
    'grade': [45.0, 42.3, 44.7, 48.5, 47.2],
}

students = pd.DataFrame(data)

# Call the function
changeDatatype(students)
