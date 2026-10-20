"""Concatenate the DataFrames along the rows axis example."""
import pandas as pd

# Create a DataFrame from a dictionary
df1 = pd.DataFrame(
    {"Nombre": ["Carmen", "Luis", "María"], "Sexo": ["Mujer", "Hombre", "Mujer"]}
).set_index("Nombre")

# Create aother DataFrame from a dictionary
df2 = pd.DataFrame(
    {"Nombre": ["Carmen", "Luis", "María"], "Edad": [22, 18, 25]}
).set_index("Nombre")

# Concatenate the DataFrames along the rows axis
df = pd.concat([df1, df2], axis=1)

# Print the DataFrame
print(df)
