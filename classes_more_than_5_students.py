"""
LeetCode
596. Classes More Than 5 Students
30 Days of Pandas
jramaswami
"""


import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class').count().reset_index().rename(columns={'student': 'count'})
    courses = courses.loc[courses['count'] >= 5].drop(columns=['count'])
    return courses