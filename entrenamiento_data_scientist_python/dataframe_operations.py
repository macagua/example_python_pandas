"""Perform some operations on the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the DataFrame
print(df)

# Multiplying the 'altura' column by 100
print(df["altura"] * 100)

# Printing just the 'sexo' column which is equal to 'M'
print(df["sexo"] == "M")
