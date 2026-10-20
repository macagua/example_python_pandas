"""Perform some functions on the DataFrame example."""
import pandas as pd
from math import log

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the DataFrame
print(df)

# Apply the logarithm function to each element in the 'altura' column
print(df["altura"].apply(log))
