"""Find big countries in the DataFrame example."""
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """Find big countries in the DataFrame

    Args:
        world (pd.DataFrame): The DataFrame containing world data

    Returns:
        pd.DataFrame: The DataFrame with big countries
    """
    return world[
        (world['area'] >= 3_000_000) | \
        (world['population'] >= 25_000_000)
    ][['name', 'population', 'area']]

# Sample Data
data = [
    ['Colombia', 'America', 652230, 25500100, 20343000000],
    ['Chile', 'America', 28748, 2831741, 12960000000],
    ['EE.UU.', 'America', 2381741, 37100000, 188681000000],
    ['Espana', 'Europe', 468, 78115, 3712000000],
    ['Venezuela', 'America', 1246700, 20609294, 100990000000]
]

world = pd.DataFrame(
    data,
    columns=['name', 'continent', 'area', 'population', 'gdp']
).astype(
    {
        'name':'object',
        'continent':'object',
        'area':'Int64',
        'population':'Int64',
        'gdp':'Int64'
    }
)

# Call the function
big_countries(world)
