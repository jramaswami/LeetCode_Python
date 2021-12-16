"""
LeetCode :: December 2021 Challenge :: 310. Minimum Height Trees
jramaswami
"""


import collections


class Solution:
    def findMinHeightTrees(self, node_count, edges):
        # Convert edges into an adjacency list.
        adj = [[] for _ in range(node_count)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(root, dist):
            "BFS to get distance from root."
            visited = [False for _ in dist]
            queue = collections.deque()
            queue.append((root, 0))
            visited[root] = True
            while queue:
                node, d = queue.popleft()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        dist[neighbor] = max(dist[neighbor], d + 1)
                        visited[neighbor] = True
                        queue.append((neighbor, d + 1))

        # Get the max of distances from each root node for every node.
        dist = [0 for _ in adj]
        for root, _ in enumerate(adj):
            bfs(root, dist)

        # The middle of the tree are the nodes with the smallest maximum
        # distance from each root node.
        k = min(dist)
        return [node for node, d in enumerate(dist) if d == k]


def test_1():
    n = 4
    edges = [[1,0],[1,2],[1,3]]
    expected = [1]
    assert Solution().findMinHeightTrees(n, edges) == expected


def test_2():
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    expected = [3,4]
    assert Solution().findMinHeightTrees(n, edges) == expected


def test_3():
    n = 1
    edges = []
    expected = [0]
    assert Solution().findMinHeightTrees(n, edges) == expected


def test_4():
    n = 2
    edges = [[0,1]]
    expected = [0,1]
    assert Solution().findMinHeightTrees(n, edges) == expected
