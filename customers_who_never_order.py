"""
LeetCode
183. Customers Who Never Order
30 Days of Pandas
jramaswami
"""


import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, how='outer', left_on='id', right_on='customerId')
    df = df.loc[pd.isnull(df['id_y'])]
    df = df[['name']]
    df = df.rename(columns={'name': 'Customers'})
    return df
