"""Find classes with at least 5 students example."""
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    """Find classes with at least 5 students.

    Args:
        courses (pd.DataFrame): DataFrame containing course enrollment data.

    Returns:
        pd.DataFrame: DataFrame with classes that have at least 5 students.
    """
    # Group the courses DataFrame by 'class' and count the number of students in each class
    courses_grouped = courses.groupby('class')['student'].size().reset_index()
    # Return only the classes that have at least 5 students, selecting only the 'class' column
    return courses_grouped[courses_grouped.student >= 5].iloc[:,[0]]

# Sample Data
courses_data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math'],
}
courses = pd.DataFrame(courses_data)

# Call the function
find_classes(courses)
