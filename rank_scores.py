"""
LeetCode
178. Rank Scores
30 Days of Pandas
jramaswami
"""


import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.assign(rank=scores['score'].rank(method='dense', ascending=False))
    scores = scores.sort_values(by='rank')
    scores = scores[['score', 'rank']]
    return scores