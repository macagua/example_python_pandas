"""Name-based access to the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the original DataFrame
print(df)

# Accessing a single column by name
print(df.loc[2, "colesterol"])

# Accessing multiple columns by name
print(df.loc[:3, ("colesterol", "peso")])

# Accessing rows by index
print(df["colesterol"])
