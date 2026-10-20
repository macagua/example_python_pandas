""""Drop missing values from a series example."""
import pandas as pd
import numpy as np

# Create a series from a list of strings with some missing values
s = pd.Series(["a", "b", None, "c", np.NaN, "d"])

# Print the original series and the series after dropping missing values
print(s)

# Drop missing values using dropna() method
print(s.dropna())
