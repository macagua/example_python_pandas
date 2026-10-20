"""Reindexing the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Reindexing the DataFrame
print(
    df.reindex(
        index=[4, 3, 1],
        columns=["nombre", "tensión", "colesterol"]
    )
)
