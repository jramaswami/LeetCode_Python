"""
LeetCode
1148. Article Views I
30 Days of Pandas
jramaswami
"""


import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views.loc[views['author_id'] == views['viewer_id']]
    views = views[['author_id']]
    views = views.drop_duplicates()
    views = views.rename(columns={'author_id': 'id'})
    views = views.sort_values(by='id')
    return views