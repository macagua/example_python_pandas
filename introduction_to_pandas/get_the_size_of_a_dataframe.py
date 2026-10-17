"""Get the Size of a DataFrame example"""
import pandas as pd
from typing import List

def getDataframeSize(players_df: pd.DataFrame) -> List[int]:
    """Get the shape of the DataFrame

    Args:
        players_df (pd.DataFrame): A DataFrame containing player data

    Returns:
        List[int]: A list containing the number of rows and columns in the pd.DataFrame
    """
    return list(players_df.shape)

data = {
    'player_id': [1, 2, 3],
    'name': ['Miguelito', 'Dieguito', 'Leonado'],
    'age': [25, 30, 22],
    'position': ['Goalkeeper', 'Forward', 'Goalie']
}

players = pd.DataFrame(data)
print(getDataframeSize(players))
