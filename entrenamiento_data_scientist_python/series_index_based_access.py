"""Index-based access in a series from a dictionary example."""
import pandas as pd

# Create a series from a dictionary
s = pd.Series({"Matemáticas": 6.0, "Economía": 4.5, "Programación": 8.5})
print(s[1:3])
# Accessing elements by index
print(s['Economía'])
# Accessing elements by label
print(s[["Programación", "Matemáticas"]])
