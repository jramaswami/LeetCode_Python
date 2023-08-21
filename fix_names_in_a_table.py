"""
LeetCode
1667. Fix Names in a Table
30 Days of Pandas
jramaswami
"""


import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users = users.assign(name=users['name'].str.capitalize())
    users = users.sort_values('user_id')
    return users