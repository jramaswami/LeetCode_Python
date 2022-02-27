"""
LeetCode :: February 2022 Challenge :: 847. Shortest Path Visiting All Nodes
jramaswami
"""


import math
import collections


class Solution:

    def shortestPathLength(self, graph):
        "BFS Solution"

        ALL_NODES_VISITED = (1 << (len(graph))) - 1

        def bfs(root):
            queue = collections.deque()
            queue.append((root, 1 << root, 0))
            visited_states = set()
            visited_states.add((root, 1 << root))
            while queue:
                node, visited_nodes, edge_count = queue.popleft()
                if visited_nodes == ALL_NODES_VISITED:
                    return edge_count

                for neighbor in graph[node]:
                    mask = 1 << neighbor
                    visited_nodes0 = visited_nodes | mask
                    if (neighbor, visited_nodes0) not in visited_states:
                        visited_states.add((neighbor, visited_nodes0))
                        queue.append((neighbor, visited_nodes0, edge_count+1))
            return math.inf

        soln = math.inf
        for root, _ in enumerate(graph):
            soln = min(soln, bfs(root))
        return soln


def test_1():
    graph = [[1,2,3],[0],[0],[0]]
    expected = 4
    assert Solution().shortestPathLength(graph) == expected


def test_2():
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    expected = 4
    assert Solution().shortestPathLength(graph) == expected


def test_3():
    "Complete graph."
    graph = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    expected = 11
    assert Solution().shortestPathLength(graph) == expected
