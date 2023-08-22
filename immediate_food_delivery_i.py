"""
LeetCode
1173. Immediate Food Delivery I
30 Days of Pandas
jramaswami
"""


import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    total = delivery.shape[0]
    delivery = delivery.loc[
        delivery['order_date'] == delivery['customer_pref_delivery_date']
    ]
    immediate = delivery.shape[0]
    pct = round(100 * immediate / total, 2)
    return pd.DataFrame({'immediate_percentage': [pct]})