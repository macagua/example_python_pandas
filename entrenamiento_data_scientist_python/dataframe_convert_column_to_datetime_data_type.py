"""Convert 'Nacimiento' column to datetime data example."""
import pandas as pd

# Create a DataFrame from a dictionary
df = pd.DataFrame(
    {
        "Name": ["María", "Carlos", "Carmen"],
        "Nacimiento": ["05-03-2000", "20-05-2001", "10-12-1999"],
    }
)

# Print the DataFrame
print(df)

# Convert 'Nacimiento' column to datetime data
print(pd.to_datetime(df.Nacimiento, format="%d-%m-%Y"))

# Print the updated DataFrame
print(df)
