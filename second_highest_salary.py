"""
LeetCode
176. Second Highest Salary
30 Days of Pandas
jramaswami
"""


import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    column_name = f'SecondHighestSalary'
    employee = employee[['salary']]
    employee = employee.drop_duplicates()
    if employee.shape[0] < 2:
        return pd.DataFrame({column_name: [None]})
    employee = employee.nlargest(2, 'salary')
    employee = employee.nsmallest(1, 'salary')
    employee = employee.rename({'salary': column_name})
    employee[column_name] = employee['salary']
    employee = employee[[column_name]]
    return employee