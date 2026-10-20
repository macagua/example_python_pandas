"""Perform some functions on the series example."""
import pandas as pd
from math import log

# Create a series from a list of integers
s = pd.Series([1, 2, 3, 4])

# Apply the logarithm function to each element in the series
s.apply(log)

# Create a series from a list of strings
s = pd.Series(["a", "b", "c"])

# Apply the upper() method to each element in the series
s.apply(str.upper)
