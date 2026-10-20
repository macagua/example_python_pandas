"""Perform sorting on the series example."""
import pandas as pd

# Create a series from a dictionary
s = pd.Series({"Matemáticas": 6.0, "Economía": 4.5, "Programación": 8.5})

# Sort the series by values and by index in descending order
print(s.sort_values())

# Sort the series by index in descending order
print(s.sort_index(ascending=False))
