"""
LeetCode
1795. Rearrange Products Table
30 Days of Pandas
jramaswami
"""


import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(
        id_vars=['product_id'],
        value_vars=['store1', 'store2', 'store3']
    )
    products = products.rename(columns={'variable': 'store', 'value': 'price'})
    products = products.dropna()
    return products