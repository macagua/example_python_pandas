"""Perform filters on the series example."""
import pandas as pd

# Create a series from a dictionary
s = pd.Series({"Matemáticas": 6.0, "Economía": 4.5, "Programación": 8.5})

# Filter the series to get only the elements greater than 5
print(s[s > 5])
