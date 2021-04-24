"""
Leet Code :: April 2021 Challenge :: Critical Connections in a Network
jramaswami
"""
from typing import *


def find_bridges(adj):
    """Find the bridges in the graph using Tarjan's algorithm."""
    discovery = [-1 for _ in adj]
    low = [-1 for _ in adj]
    timer = 0
    soln = []

    def dfs(node, parent):
        """Helper function: dfs to find bridges"""
        nonlocal timer
        timer = timer + 1
        discovery[node] = low[node] = timer
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if discovery[neighbor] == -1:
                dfs(neighbor, node)
                if discovery[node] < low[neighbor]:
                    soln.append([node, neighbor])
                low[node] = min(low[node], low[neighbor])
            else:
                low[node] = min(low[node], discovery[neighbor])

    # Look for bridges in every connected component.
    for u, _ in enumerate(adj):
        if discovery[u] == -1:
            dfs(u, -1)

    return soln


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Prepare adjacency list.
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        return find_bridges(adj)


def test_1():
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    assert Solution().criticalConnections(n, connections) == [[1, 3]]