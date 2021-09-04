"""
LeetCode :: September 2021 Challenge :: Sum of Distances in Tree
jramaswami

REF: https://cp-algorithms.com/graph/lca.html
"""


class LCA:

    def __init__(self, adj, root = 0):
        self.adj = adj
        self.height = [0 for _ in adj]
        self.first = [0 for _ in adj]
        self.euler = []
        self.visited = [False for _ in adj]
        self.dfs(root)
        self.segtree = [0 for _ in range(4 * len(self.euler))]
        self.build(1, 0, len(self.euler) - 1)

    def dfs(self, node, ht = 0):
        self.visited[node] = True
        self.height[node] = ht
        self.first[node] = len(self.euler)
        self.euler.append(node)
        for neighbor in self.adj[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, ht + 1)
                self.euler.append(node)

    def build(self, node, b, e):
        if b == e:
            self.segtree[node] = self.euler[b]
        else:
            mid = (b + e) // 2
            left_child = node << 1
            right_child = (node << 1) | 1
            self.build(left_child, b, mid)
            self.build(right_child, mid + 1, e)
            left_value = self.segtree[left_child]
            right_value = self.segtree[right_child]
            if self.height[left_value] < self.height[right_value]:
                self.segtree[node] = left_value
            else:
                self.segtree[node] = right_value

    def query(self, node, b, e, L, R):
        if b > R or e < L:
            return -1
        if b >= L and e <= R:
            return self.segtree[node]

        mid = (b + e) >> 1;
        left = self.query(node << 1, b, mid, L, R)
        right = self.query((node << 1) | 1, mid + 1, e, L, R)
        if left == -1:
            return right
        if right == -1:
            return left
        if self.height[left] < self.height[right]:
            return left
        else:
            return right

    def lca(self, u, v):
        left = self.first[u]
        right = self.first[v]
        if left > right:
            left, right = right, left
        return self.query(1, 0, len(self.euler) - 1, left, right)

    def get_distance(self, u, v):
        lca = self.lca(u, v)
        # Distance from root to u + distance from root to u - distance
        # from root to the lca (which was counted twice).
        dist = self.height[u] + self.height[v] - (2 * self.height[lca])
        return dist



class Solution:

    def sumOfDistancesInTree(self, node_count, edges):
        adj = [[] for _ in range(node_count)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        lca = LCA(adj)

        soln = [0 for _ in adj]
        for u in range(node_count):
            for v in range(u + 1, node_count):
                d = lca.get_distance(u, v)
                soln[u] += d
                soln[v] += d
        return soln


def test_1():
    node_count= 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    expected = [8,12,6,10,10,10]
    assert Solution().sumOfDistancesInTree(node_count, edges) == expected


def test_2():
    node_count = 1
    edges = []
    expected = [0]
    assert Solution().sumOfDistancesInTree(node_count, edges) == expected


def test_3():
    node_count = 2
    edges = [[1,0]]
    expected = [1,1]
    assert Solution().sumOfDistancesInTree(node_count, edges) == expected
