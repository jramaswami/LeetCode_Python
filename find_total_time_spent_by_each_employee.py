"""
LeetCode
1741. Find Total Time Spent by Each Employee
30 Days of Pandas
jramaswami
"""


import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.assign(
        event_time = employees.out_time - employees.in_time
    )
    employees = employees[['event_day', 'emp_id', 'event_time']]
    employees = employees.groupby(['event_day', 'emp_id']).sum().reset_index()
    employees = employees.rename(
        columns={'event_day': 'day', 'event_time': 'total_time'}
    )
    return employees