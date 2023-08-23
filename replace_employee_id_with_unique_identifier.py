"""
LeetCode
1378. Replace Employee ID With The Unique Identifier
30 Days of Pandas
jramaswami
"""


import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    employees = employees.merge(employee_uni, how='left')
    employees = employees[['unique_id', 'name']]
    return employees