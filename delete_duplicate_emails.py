"""
LeetCode
196. Delete Duplicate Emails
30 Days of Pandas
jramaswami
"""


import pandas as pd


# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', inplace=True)
    person.drop_duplicates('email', keep='first', inplace=True)