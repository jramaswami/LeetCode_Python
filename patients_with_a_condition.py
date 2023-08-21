"""
LeetCode
1527. Patients With a Condition
30 Days of Pandas
jramaswami
"""


import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients = patients.loc[patients['conditions'].str.contains(r'\bDIAB1')]
    return patients