"""
LeetCode :: February 2022 Challenge :: 133. Clone Graph
jramaswami


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


import collections


class Solution:

    def cloneGraph(self, root):
        # Boundary case:
        if root is None:
            return None

        # Build an adjacency list.
        adj = collections.defaultdict(list)
        queue = collections.deque()
        queue.append(root)
        visited = set()
        visited.add(root.val)
        nodes = dict()
        while queue:
            node = queue.popleft()
            nodes[node.val] = Node(node.val, [])
            for neighbor in node.neighbors:
                adj[node.val].append(neighbor.val)
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append(neighbor)

        # Clone graph using adjacency list.
        for val, neighbors in adj.items():
            for neighbor in neighbors:
                nodes[val].neighbors.append(nodes[neighbor])
        return nodes[root.val]
