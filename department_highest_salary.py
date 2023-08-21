"""
LeetCode
184. Department Highest Salary
30 Days of Pandas
jramaswami
"""


import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=['_employee', '_department'])
    df = df[['name_department', 'name_employee', 'salary']]
    df = df.rename(
        columns={
            'name_department': 'Department',
            'name_employee': 'Employee',
            'salary': 'Salary'
        }
    )
    # Get a dataframe with the maximum salary by department
    max_df = df[['Department', 'Salary']]
    max_df = max_df.groupby(by='Department').max().reset_index()
    # Inner join df to max_df which will filter out anyone that doesn't have the max salary
    df = df.merge(max_df)
    return df