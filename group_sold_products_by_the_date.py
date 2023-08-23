"""
LeetCode
1484. Group Sold Products By The Date
30 Days of Pandas
jramaswami
"""


import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # Prevent product from showing up more than once
    activities = activities.drop_duplicates()
    # Make sure concatenated list is sorted
    activities = activities.sort_values(by=['product'])
    # Concatenate list
    activities = activities.groupby(['sell_date']).agg({'product': ['count', ','.join]}).reset_index()
    # Flatten multiindex
    activities.columns = ['sell_date', 'num_sold', 'products']
    return activities