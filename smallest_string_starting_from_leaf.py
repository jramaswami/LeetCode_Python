"""
LeetCode
988. Smallest String Starting From Leaf
April 2024 Challenge
jramaswami
"""


import collections
import heapq


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        queue = []

        # Turn into a graph and then do a BFS
        parents = []
        values = []

        ord_a = ord('a')

        def rec(node, p):
            if node is None:
                return

            node_id = len(values)
            values.append(chr(ord_a + node.val))
            parents.append(p)

            if node.left is None and node.right is None:
                # Leaf node
                heapq.heappush(queue, (values[-1], node_id))

            rec(node.left, node_id)
            rec(node.right, node_id)

        rec(root, -1)

        # Dijkstra's to find minimum string
        while queue:
            s, node_id = heapq.heappop(queue)
            if parents[node_id] == -1:
                return s
            p = parents[node_id]
            heapq.heappush(queue, (s + values[p], p))