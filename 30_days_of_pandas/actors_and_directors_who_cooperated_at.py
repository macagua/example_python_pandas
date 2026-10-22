"""Actors and Directors Who Cooperated At Least Three Times example."""
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    """Actors and Directors Who Cooperated At Least Three Times

    Args:
        actor_director (pd.DataFrame): DataFrame object containing columns 'actor_id' and 'director_id'

    Returns:
        pd.DataFrame: DataFrame filtered to include only those pairs where the number of cooperation
    """
    # Group the data by actor_id and director_id, and count the number of cooperations
    df_grouped = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
    # Filter the pairs where the cooperation count is at least three
    df_filtered = df_grouped[df_grouped['cooperation_count'] >= 3]
    return df_filtered[['actor_id', 'director_id']]

# Sample Data
data = {
    'actor_id': [1, 1, 1, 1, 1, 2, 2],
    'director_id': [1, 1, 1, 2, 2, 1, 1],
    'timestamp': [0, 1, 2, 3, 4, 5, 6],
}
actor_director = pd.DataFrame(data)

# Call the function
actors_and_directors(actor_director)
