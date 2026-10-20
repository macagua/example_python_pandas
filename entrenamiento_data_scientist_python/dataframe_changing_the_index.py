"""Changing the index of the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Changing the index of the DataFrame
print(df.set_index("nombre").head())
