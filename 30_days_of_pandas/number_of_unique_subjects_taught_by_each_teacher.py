"""Count the number of unique subjects taught by each teacher example"""
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    """Count the number of unique subjects taught by each teacher.

    Args:
        teacher (pd.DataFrame): DataFrame containing teacher subject data.

    Returns:
        pd.DataFrame: DataFrame with each teacher's unique subject count.
    """
    # Count the number of unique subjects taught by each teacher.
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    # Rename the columns to 'teacher_id' and 'cnt' for clarity.
    result.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return result

# Sample Data
data = {
    'teacher_id': [1, 1, 1, 2, 2, 2, 2],
    'subject_id': [2, 2, 3, 1, 2, 3, 4],
    'dept_id': [3, 4, 3, 1, 1, 1, 1],
}
teacher = pd.DataFrame(data)

# Call the function
count_unique_subjects(teacher)
