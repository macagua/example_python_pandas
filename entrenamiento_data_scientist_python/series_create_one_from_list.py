"""Create a series from a list example."""
import pandas as pd

# Create a series from a list
s = pd.Series(
    ["Matemáticas", "Historia", "Economía", "Programación", "Inglés"],
    dtype="string"
)

# Print the series
print(s)
