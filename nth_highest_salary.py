"""
LeetCode
177. Nth Highest Salary
30 Days of Pandas
jramaswami
"""


import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    column_name = f'getNthHighestSalary({N})'
    employee = employee[['salary']]
    employee = employee.drop_duplicates()
    if employee.shape[0] < N:
        return pd.DataFrame({column_name: [None]})
    employee = employee.nlargest(N, 'salary')
    employee = employee.nsmallest(1, 'salary')
    employee = employee.rename({'salary': column_name})
    return employee