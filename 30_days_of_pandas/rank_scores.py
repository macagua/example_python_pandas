"""Order scores in descending order and assign ranks example"""
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """Order scores in descending order and assign ranks.

    Args:
        scores (pd.DataFrame): DataFrame containing scores.

    Returns:
        pd.DataFrame: DataFrame with ordered scores and assigned ranks.
    """
    # Assign ranks using the 'dense' method, which assigns the same rank to tied scores and does not skip ranks
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    # Sort the scores in descending order and return the relevant columns
    return scores.sort_values('score', ascending=False)[['score', 'rank']]

scores_data = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}
scores = pd.DataFrame(scores_data)

# Call the function
order_scores(scores)
