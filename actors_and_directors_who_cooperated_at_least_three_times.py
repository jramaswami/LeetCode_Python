"""
LeetCode
1050. Actors and Directors Who Cooperated At Least Three Times
30 Days of Pandas
jramaswami
"""


import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = (actor_director
        .groupby(['actor_id', 'director_id'])
        .count()
        .reset_index()
        .rename(columns={'timestamp': 'collaborations'})
    )
    actor_director = actor_director.loc[actor_director['collaborations'] >= 3]
    actor_director = actor_director.drop(columns=['collaborations'])
    return actor_director