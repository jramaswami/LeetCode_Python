"""
LeetCode
2082. The Number of Rich Customers
30 Days of Pandas
jramaswami
"""


import pandas as pd


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store = store.loc[store['amount'] > 500]
    store = store[['customer_id']].drop_duplicates('customer_id')
    rich_count = store.shape[0]
    return pd.DataFrame({'rich_count': [rich_count]})