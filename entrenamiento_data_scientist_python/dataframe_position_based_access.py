"""Position-based access to the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the original DataFrame
print(df)

# Position-based access to the DataFrame
print(df.iloc[1, 3])
print(df.iloc[1, :2])
