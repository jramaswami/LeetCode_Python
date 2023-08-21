"""
LeetCode
1148. Article Views I
30 Days of Pandas
jramaswami
"""


import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets = tweets.loc[tweets['content'].str.len() > 15]
    tweets = tweets[['tweet_id']]
    return tweets