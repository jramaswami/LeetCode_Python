"""
LeetCode
586. Customer Placing the Largest Number of Orders
30 Days of Pandas
jramaswami
"""


import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number').count().reset_index().rename(columns={'order_number': 'order_count'})
    orders = orders.nlargest(n=1, columns='order_count')
    orders = orders[['customer_number']]
    return orders