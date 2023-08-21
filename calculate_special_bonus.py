"""
LeetCode
1873. Calculate Special Bonus
30 Days of Pandas
jramaswami
"""


import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']
    employees['bonus'] = employees['bonus'].where(employees['employee_id'] % 2 == 1, 0)
    employees['bonus'] = employees['bonus'].mask(employees['name'].str.startswith('M'), 0)
    employees = employees[['employee_id', 'bonus']]
    employees = employees.sort_values('employee_id')
    return employees