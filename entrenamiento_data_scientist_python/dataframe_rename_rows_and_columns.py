"""Renaming rows and columns in the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Renaming rows and columns in the DataFrame
print(
    df.rename(
        columns={"nombre": "nombre y apellidos", "altura": "estatura"},
        index={0: 1000, 1: 1001, 2: 1002},
    )
)
