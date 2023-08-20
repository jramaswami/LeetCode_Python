"""
LeetCode
595. Big Countries
30 Days of Pandas
jramaswami
"""


import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world.loc[(world.area >= 3_000_000) | (world.population >= 25_000_000)]
    world = world[['name', 'population', 'area']]
    return world