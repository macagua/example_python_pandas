"""Create a DataFrame from a CSV file and export to an Excel spreadsheet file example."""
import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv(
    "https://raw.githubusercontent.com/macagua/entrenamiento.data_scientist_python/main/recursos/leccion3/datos/colesteroles.csv",
    sep=";",
    decimal=",",
)

# Displaying the first 5 rows of the DataFrame
print(df.head())

# Exporting the DataFrame to an Excel spreadsheet file
df.to_excel(
    'analisis_colesterol.xlsx',
    sheet_name='Analisis_colesterol',
    header=True,
    index=False
)
