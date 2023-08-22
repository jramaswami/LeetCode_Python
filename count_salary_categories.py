"""
LeetCode
1907. Count Salary Categories
30 Days of Pandas
jramaswami
"""


import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts = accounts.assign(category = 'Low Salary')
    accounts = accounts.assign(
        category = accounts['category'].mask(
            accounts['income'] >= 20_000,
            'Average Salary'
        )
    )
    accounts = accounts.assign(
        category = accounts['category'].mask(
            accounts['income'] > 50_000,
            'High Salary'
        )
    )
    accounts = accounts.drop(columns=['account_id'])
    accounts = accounts.groupby(by='category').count().reset_index()
    accounts = accounts.rename(columns={'income': 'accounts_count'})
    accounts = accounts.merge(
        pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary']}),
        how='right'
    )
    accounts = accounts.fillna(0)
    return accounts