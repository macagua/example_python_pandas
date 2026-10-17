"""Concatenate two DataFrames vertically example"""
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Concatenate two DataFrames vertically

    Args:
        df1 (pd.DataFrame): The first DataFrame
        df2 (pd.DataFrame): The second DataFrame

    Returns:
        pd.DataFrame: The concatenated DataFrame
    """
    df = pd.concat([df1, df2])
    return df

# Sample Data
data1 = {
    'student_id': [1, 2, 3],
    'name': ['Leonaroo', 'Ana', 'Hectmar'],
    'age': [45, 42, 44],
}
students1 = pd.DataFrame(data1)

data2 = {
    'student_id': [4, 5],
    'name': ['Diego', 'Rafael'],
    'age': [48, 4],
}
students2 = pd.DataFrame(data2)

# Call the function
concatenateTables(students1, students2)
