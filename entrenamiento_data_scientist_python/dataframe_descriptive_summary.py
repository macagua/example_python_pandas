"""Descriptive summary of the DataFrame example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesterol.csv"
)

# Print the DataFrame
print(df)

# Count item in 'edad' column
print(df.edad.count())

# Mean in 'edad' column
print(df.edad.mean())

# Variance in 'edad' column
print(df.edad.var())

# Standard deviation in 'edad' column
print(df.edad.std())

# Covariance matrix
df.cov()

# Correlation matrix
print(df.corr())

# Descriptive summary
print(df.describe())

# Descriptive summary por tipo de dato
print(df.describe(include="object"))
