"""
LeetCode
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
July 2024 Challenge
jramaswami
"""


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = pow(10,10)
        # Floyd Warshall
        dist = [[INF for _ in range(n)] for _ in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for v in range(n):
            dist[v][v] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        soln = -1
        min_cities = INF
        for u in range(n):
            can_reach = 0
            for v in range(n):
                if dist[u][v] <= distanceThreshold:
                    can_reach += 1
            if can_reach <= min_cities:
                soln, min_cities = u, can_reach
        return soln