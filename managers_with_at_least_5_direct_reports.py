"""
LeetCode
570. Managers with at Least 5 Direct Reports
30 Days of Pandas
jramaswami
"""


import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(employee, how='inner', left_on='id', right_on='managerId', suffixes=['_mgr', '_emp'])
    employee = employee[['id_mgr', 'name_mgr', 'id_emp']]
    employee = employee.groupby(['id_mgr', 'name_mgr']).count().reset_index().rename(columns={'id_emp': 'subordinates'})
    employee = employee.loc[employee['subordinates'] >= 5]
    employee = employee[['name_mgr']]
    employee = employee.rename(columns={'name_mgr': 'name'})
    return employee