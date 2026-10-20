"""Concatenate the DataFrames along the columns axis example."""
import pandas as pd

# Create a DataFrame from a dictionary
df1 = pd.DataFrame(
    {"Nombre": ["Carmen", "Luis"], "Sexo": ["Mujer", "Hombre"], "Edad": [22, 18]}
).set_index("Nombre")

# Create aother DataFrame from a dictionary
df2 = pd.DataFrame(
    {"Nombre": ["María", "Pedro"], "Sexo": ["Mujer", "Hombre"], "Edad": [25, 30]}
).set_index("Nombre")

# Concatenate the DataFrames along the columns axis
df = pd.concat([df1, df2])

# Print the DataFrame
print(df)
