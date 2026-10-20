"""Filtering rows based on conditions example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the DataFrame
print(df)

# Filtering rows based on conditions
print(df[(df["sexo"] == "H") & (df["colesterol"] > 260)])
