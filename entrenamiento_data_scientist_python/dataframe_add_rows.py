"""Adding a new row to the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the DataFrame
print(df)

# Adding a new row to the DataFrame
df = df.append(
    # Create a new row as a Series
    pd.Series(
        ["Carlos Rivas", 28, "H", 89.0, 1.78, 245.0],
        index=["nombre", "edad", "sexo", "peso", "altura", "colesterol"],
    ),
    ignore_index=True,
)

# Printing the updated DataFrame
print(df.tail())
