"""Group by DataFrame columns example."""

import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the DataFrame
print(df)

# Group by a column
print(df.groupby("sexo").groups)

# Group by multiple columns
print(df.groupby(["sexo", "edad"]).groups)
