"""
LeetCode
2356. Number of Unique Subjects Taught by Each Teacher
30 Days of Pandas
jramaswami
"""


import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.drop(columns=['dept_id'])
    teacher = teacher.drop_duplicates()
    teacher = teacher.groupby(['teacher_id']).count().reset_index()
    teacher = teacher.rename(columns={'subject_id': 'cnt'})
    return teacher