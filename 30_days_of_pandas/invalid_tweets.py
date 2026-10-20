"""Find invalid tweets based on content length example."""
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    """Find invalid tweets based on content length.

    Args:
        tweets (pd.DataFrame): DataFrame containing tweet data.

    Returns:
        pd.DataFrame: DataFrame with IDs of invalid tweets.
    """
    df_invalid = tweets[tweets['content'].str.len() > 15]
    return df_invalid[['tweet_id']]

# Sample Data
data_posts = {
    'tweet_id': [1, 2],
    'content': ['Let us Code', 'More than fifteen chars are here!'],
}
posts = pd.DataFrame(data_posts)

# Call the function
invalid_tweets(posts)
