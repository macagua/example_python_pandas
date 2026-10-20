"""Create a DataFrame from List example.""""""
from typing import List
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    """Create a DataFrame from a list of lists

    Args:
        student_data (List[List[int]]): A list of lists containing student data

    Returns:
        pd.DataFrame: A DataFrame with the student data
    """
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

students = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

createDataframe(students)
