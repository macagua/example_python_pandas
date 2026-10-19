"""Create a series from a list and access its properties example"""
import pandas as pd

# Create a series from a list
s = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(s)
# Print the size of the series
print(s.size)
# Print the index of the series
print(s.index)
# Print the data type of the series
print(s.dtype)
