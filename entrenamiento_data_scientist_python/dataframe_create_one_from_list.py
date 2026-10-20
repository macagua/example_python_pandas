"""Create a DataFrame from a list of lists example."""
import pandas as pd

# Create a DataFrame from a list of lists
df = pd.DataFrame(
    [["María", 18], ["Luis", 22], ["Carmen", 20]], columns=["Nombre", "Edad"]
)

# Print the DataFrame
print(df)
