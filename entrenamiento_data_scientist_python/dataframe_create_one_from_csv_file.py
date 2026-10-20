"""Create a DataFrame from a from a CSV file example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesteroles.csv",
    sep=";",
    decimal=",",
)

# Print the DataFrame
print(df)

# Displaying the first 5 rows of the DataFrame
print(df.head())
