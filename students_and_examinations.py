"""
LeetCode
1280. Students and Examinations
30 Days of Pandas
jramaswami
"""


import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    students = students.merge(subjects, how='cross')
    examinations = examinations.groupby(['student_id', 'subject_name']).agg({'subject_name': ['count']}).reset_index()
    examinations.columns = ['student_id', 'subject_name', 'attended_exams']
    students = students.merge(examinations, how='left')
    students = students.assign(attended_exams = students['attended_exams'].fillna(0))
    students = students.sort_values(['student_id', 'subject_name'])
    students = students[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    return students