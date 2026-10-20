"""Convert the long format DataFrame to wide format example."""
import pandas as pd

# Create a dictionary with data for the DataFrame
data = {
    "nombre": ["María", "Luis", "Carmen"],
    "edad": [18, 22, 20],
    "Matemáticas": [8.5, 7, 3.5],
    "Economía": [8, 6.5, 5],
    "Programación": [6.5, 4, 9],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame original
print(df)

# Convert the wide format DataFrame to long format
df1 = df.melt(id_vars=["nombre", "edad"], var_name="asignatura", value_name="nota")

# Print the DataFrame converted
print(df1)

# Convert the long format DataFrame to wide format
print(df1.pivot(index="nombre", columns="asignatura", values="nota"))
