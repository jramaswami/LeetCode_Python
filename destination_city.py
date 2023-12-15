"""
LeetCode
1436. Destination City
December 2023 Challenge
jramaswami
"""


import collections


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegree = collections.defaultdict(int)
        cities = set()
        for u, v in paths:
            outdegree[u] += 1
            cities.add(u)
            cities.add(v)

        for city in cities:
            if outdegree[city] == 0:
                return city