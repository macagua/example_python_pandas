"""Analyze game play data to find the first login date for each player example."""
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """Analyze game play data to find the first login date for each player.

    Args:
        activity (pd.DataFrame): DataFrame containing game play activity data.

    Returns:
        pd.DataFrame: DataFrame with each player's first login date.
    """
    # Sort the DataFrame by 'player_id' and 'event_date' to ensure the earliest date is first for each player.
    activity = activity.sort_values(by=['player_id', 'event_date'])
    # Group by 'player_id' and get the minimum 'event_date' for each player, which represents their first login date.
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    # Rename the 'event_date' column to 'first_login' for clarity.
    result.rename(columns={'event_date': 'first_login'}, inplace=True)
    return result

# Sample Data
data = {
    'player_id': [1, 1, 2, 2, 3],
    'device_id': [2, 2, 3, 1, 4],
    'event_date': [
        pd.Timestamp('2016-03-01'),
        pd.Timestamp('2016-05-02'),
        pd.Timestamp('2017-06-25'),
        pd.Timestamp('2016-03-02'),
        pd.Timestamp('2018-07-03')
    ],
    'games_played': [5, 6, 1, 0, 5],
}
activity = pd.DataFrame(data)

# Call the function
game_analysis(activity)
