"""Merge the DataFrames along the right axis example."""
import pandas as pd

# Create a DataFrame from a dictionary
df1 = pd.DataFrame(
    {"Nombre": ["Carmen", "Luis", "María"], "Sexo": ["Mujer", "Hombre", "Mujer"]}
)

# Create other DataFrame from a dictionary
df2 = pd.DataFrame({"Nombre": ["María", "Pedro", "Luis"], "Edad": [25, 30, 18]})

# Merge the DataFrames along the right axis
df = pd.merge(df1, df2, on="Nombre", how="right")

# Print the DataFrame
print(df)
