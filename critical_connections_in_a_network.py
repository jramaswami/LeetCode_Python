"""
Leet Code :: May 2022 Challenge :: Critical Connections in a Network
jramaswami
"""


import itertools


class Solution:
    def criticalConnections(self, n, connections):
        # Convert list of edges into a graph.
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        timer = itertools.count(1)
        visited = [False for _ in graph]
        time_in = [None for _ in graph]
        low = [None for _ in graph]
        soln = []

        def tarjans(node, parent):
            visited[node] = True
            time_in[node] = low[node] = next(timer)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if visited[neighbor]:
                    low[node] = min(low[node], time_in[neighbor])
                else:
                    tarjans(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[node] != low[neighbor]:
                        soln.append([min(node, neighbor), max(node,neighbor)])

        tarjans(0, -1)
        return soln


def test_1():
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    assert Solution().criticalConnections(n, connections) == [[1, 3]]
