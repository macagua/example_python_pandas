"""Find authors who have viewed their own articles example."""
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    """Find authors who have viewed their own articles

    Args:
        views (pd.DataFrame): The DataFrame containing view data

    Returns:
        pd.DataFrame: The DataFrame with authors who have viewed their own articles
    """
    # Filter the DataFrame to find rows where the author_id is equal to the viewer_id
    df = views[views['author_id'] == views['viewer_id']]
    # Select only the 'author_id' column, drop duplicates, sort the values, and rename the column to 'id'
    # Return the resulting DataFrame
    df = df[['author_id']].drop_duplicates()
    # Sort the DataFrame by 'author_id' and rename the column to 'id'
    df = df.sort_values(by='author_id')
    # Select only the 'author_id' column and rename it to 'id'
    df = df[['author_id']].rename(columns={'author_id': 'id'})
    # Return the resulting DataFrame
    return df

# Sample Data
data_views = {
    'article_id': [1, 1, 2, 2, 4],
    'author_id': [3, 3, 7, 7, 7],
    'viewer_id': [5, 6, 7, 6, 1],
    'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22'],
}
views = pd.DataFrame(data_views)

# Call the function
article_views(views)
