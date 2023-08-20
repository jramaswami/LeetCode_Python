"""
LeetCode
1757. Recyclable and Low Fat Products
30 Days of Pandas
jramaswami
"""


import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products.loc[(products.low_fats == 'Y') & (products.recyclable == 'Y')]
    products = products[['product_id']]
    return products