"""Create a DataFrame from a CSV file and access its properties example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the DataFrame
print(df)

# Displaying the first 5 rows of the DataFrame
print(df.info())

# Displaying the shape of the DataFrame
print(df.shape)

# Displaying the size of the DataFrame
print(df.size)

# Displaying the columns of the DataFrame
print(df.columns)

# Displaying the index of the DataFrame
print(df.index)

# Displaying the data types of the DataFrame
print(df.dtypes)
