"""Group by a DataFrame column and apply the NumPy mean function example."""
import pandas as pd
import numpy as np

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Group by a column and apply the NumPy mean function
print(df.groupby("sexo").agg(np.mean))
