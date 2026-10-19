"""Create a series from a list and a dictionary example"""
import pandas as pd

# Create a series from a list
s = pd.Series(
    ["Matemáticas", "Historia", "Economía", "Programación", "Inglés"], dtype="string"
)
print(s)
