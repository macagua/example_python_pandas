"""Perform arithmetic operations on the series example."""
import pandas as pd

# Create a series from a list of integers
s = pd.Series([1, 2, 3, 4])

# Multiplication operation
print(s * 2)

# Modulo operation
print(s % 2)

# Create a series from a list of strings
s = pd.Series(["a", "b", "c"])

# Multiplication operation on a series of strings
print(s * 5)
