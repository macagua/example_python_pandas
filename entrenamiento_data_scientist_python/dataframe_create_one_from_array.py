"""Create a DataFrame from a NumPy array example."""
import pandas as pd
import numpy as np

# Create a DataFrame from a NumPy array
df = pd.DataFrame(
    np.random.randn(4, 3), columns=["a", "b", "c"]
)

# Print the DataFrame
print(df)
