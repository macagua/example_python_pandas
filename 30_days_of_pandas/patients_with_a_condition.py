"""Find patients with a specific condition to start with BIAB1 example."""
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    """Find patients with a specific condition to start with BIAB1.

    Args:
        patients (pd.DataFrame): DataFrame containing patient information.

    Returns:
        pd.DataFrame: DataFrame containing only patients with the specified condition.
    """
    return patients[patients['conditions'].str.contains(r'(^| )DIAB1', regex=True, na=False)]

data = {
    'patient_id': [1, 2, 3, 4, 5],
    'patient_name': ['Leonardo', 'Ana', 'Yelitze', 'Miriam', 'Rafael'],
    'conditions': [
        'DIAB100',
        'BP500',
        'DIAB100',
        'ACNE DIAB100',
        'DIAB201'
    ],
}
patients = pd.DataFrame(data)

# Call the function
find_patients(patients)
