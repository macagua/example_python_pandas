
"""Deleting a specific column from the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Deleting a specific column from the DataFrame
edad = df.pop("edad")

# Printing the deleted column
print(edad)

# Print the DataFrame
print(df)
