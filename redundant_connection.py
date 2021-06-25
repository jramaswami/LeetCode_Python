"""
LeetCode :: June 2021 Challenge :: Redundant Connection
jramaswami
"""
class Solution:
    def findRedundantConnection(self, edges):
        """
        Use Disjoint Set Union to find the last edge that attempts to connect
        vertices that are already connected.

        This is a nearly O(n) solution as that is the time complexity of
        find_set, which is the bottleneck operation.
        """

        parent = {}
        size = {}

        def make_set(v):
            parent[v] = v
            size[v] = 1

        def find_set(v):
            if parent[v] == v:
                return v
            p = find_set(parent[v])
            parent[v] = p
            return p

        def union_set(a, b):
            a = find_set(a)
            b = find_set(b)
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]

        def connected(a, b):
            return find_set(a) == find_set(b)

        for v in range(1, len(edges) + 1):
            make_set(v)

        for a, b in edges:
            if connected(a, b):
                return (a, b)
            union_set(a, b)


def test_1():
    edges = [[1,2],[1,3],[2,3]]
    expected = [2,3]
    assert Solution().findRedundantConnection(edges)


def test_2():
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    expected = [1,4]
    assert Solution().findRedundantConnection(edges)
