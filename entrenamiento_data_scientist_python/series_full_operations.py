"""Series full operations example."""
import pandas as pd

s = pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

# Sample size
print(s.count())

# Summary statistics
print(s.sum())

# Cumulative total
print(s.cumsum())

# Absolute frequencies
print(s.value_counts())

# Relative frequencies
print(s.value_counts(normalize=True))

# Minimum
print(s.min())

# Maximum
print(s.max())

# Mean
print(s.mean())

# Standard deviation
print(s.std())

# Descriptive summary
print(s.describe())
