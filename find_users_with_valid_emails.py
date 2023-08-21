"""
LeetCode
1517. Find Users With Valid E-Mails
30 Days of Pandas
jramaswami
"""


import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    domain = '@leetcode.com'
    users = users.loc[users['mail'].str.endswith(domain)]
    users = users.assign(prefix=(users['mail'].str[:-len(domain)]))
    users = users.loc[~users['prefix'].str.contains('[^A-Za-z0-9_.-]')]
    users = users.loc[users['prefix'].str[0].str.isalpha()]
    users = users.drop(columns=['prefix'])
    return users