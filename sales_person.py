"""
LeetCode
607. Sales Person
30 Days of Pandas
jramaswami
"""


import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_sales_person = sales_person.merge(orders)
    red_sales_person = red_sales_person.merge(company, left_on='com_id', right_on='com_id')
    red_sales_person = red_sales_person.loc[red_sales_person['name_y'] == 'RED']
    red_sales_person = red_sales_person[['sales_id']]
    red_sales_person = red_sales_person.assign(red=1)
    sales_person = sales_person.merge(red_sales_person, how='left')
    sales_person = sales_person.loc[sales_person['red'].isnull()]
    sales_person = sales_person[['name']]
    return sales_person