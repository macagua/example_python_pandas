"""Find heavy animals in the DataFrame example"""
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """Find heavy animals in the DataFrame

    Args:
        animals (pd.DataFrame): The DataFrame containing animal data

    Returns:
        pd.DataFrame: The DataFrame with heavy animals
    """
    return animals[animals["weight"] > 100].sort_values("weight", ascending=False)[["name"]]

# Sample Data
data = {
    'name': ['Leonardo', 'Ana', 'Hectmar', 'Diego', 'Rafael'],
    'species': ['Snake', 'Bear', 'Cat', 'Leopard', 'Giraffe'],
    'age': [13, 23, 3, 5, 34],
    'weight': [63, 54, 783, 553, 349],
}

animals = pd.DataFrame(data)

# Call the function
findHeavyAnimals(animals)
