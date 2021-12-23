"""
LeetCode :: December 2021 Challenge :: 210. Course Schedule II
jramaswami
"""


import collections


WHITE, GRAY, BLACK = (0, 1, 2)


class Solution:

    def findOrder(self, node_count, edges):

        def dfs(node, adj, colors, acc):
            if color[node] == BLACK:
                return True

            if color[node] == GRAY:
                # Not a DAG!
                return False

            color[node] = GRAY
            dag = True
            for neighbor in adj[node]:
                dag = dfs(neighbor, adj, color, acc)
                if not dag:
                    break

            color[node] = BLACK
            acc.appendleft(node)
            return dag

        # Convert edges into graph.
        adj = [[] for _ in range(node_count)]
        for u, v in edges:
            adj[v].append(u)

        color = [WHITE for _ in adj]
        acc = collections.deque()
        for node, _ in enumerate(adj):
            if color[node] == WHITE:
                dag = dfs(node, adj, color, acc)
                if not dag:
                    return []
        return list(acc)


def test_1():
    node_count = 2
    edges = [[1,0]]
    expected = [0, 1]
    assert Solution().findOrder(node_count, edges) == expected


def test_2():
    node_count = 4
    edges = [[1,0],[2,0],[3,1],[3,2]]
    expected = [[0,2,1,3], [0,1,2,3], [0,2,1,3]]
    assert Solution().findOrder(node_count, edges) in expected
