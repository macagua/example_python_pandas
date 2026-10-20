"""Adding a new column to the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the DataFrame
print(df)

# Adding a new column to the DataFrame
df["diabetes"] = pd.Series([False, False, True, False, True])

# Print the DataFrame with the new column
print(df)
