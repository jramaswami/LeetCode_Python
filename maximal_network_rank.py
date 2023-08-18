"""
LeetCode
1615. Maximal Network Rank
August 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0 for _ in range(n)]
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for u, v in roads:
            indegree[u] += 1
            indegree[v] += 1
            adj_matrix[u][v] += 1
            adj_matrix[v][u] += 1

        soln = 0
        for u in range(n):
            for v in range(u+1,n):
                network_range = indegree[u] + indegree[v] - adj_matrix[u][v]
                soln = max(soln, network_range)
        return soln


def test_1():
    n = 4
    roads = [[0,1],[0,3],[1,2],[1,3]]
    expected = 4
    assert Solution().maximalNetworkRank(n, roads) == expected


def test_2():
    n = 5
    roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
    expected = 5
    assert Solution().maximalNetworkRank(n, roads) == expected


def test_3():
    n = 8
    roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    expected = 5
    assert Solution().maximalNetworkRank(n, roads) == expected