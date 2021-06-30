"""
LeetCode :: June 2021 Challenge :: Lowest Common Ancestor of a Binary Tree
jramaswami
"""


from collections import deque


class Solution():
    def lowestCommonAncestor(self, root, p_node, q_node):
        # First, use a BFS to traverse tree and assign a level to each node
        # and a parent for each node.  Dictionaries can be used for this
        # because node values are unique.  Each node is enqueued for an O(N)
        # time complexity.  With level, parent, and queue we need O(N) extra
        # space.
        level = dict()
        parent = dict()
        queue = deque()
        queue.append((root, 0))
        parent[root] = None
        while queue:
            node, lvl = queue.popleft()
            level[node] = lvl
            if node.left is not None:
                parent[node.left] = node
                queue.append((node.left, lvl+1))
            if node.right is not None:
                parent[node.right] = node
                queue.append((node.right, lvl+1))

        # Finding the LCA will at most require traversing the entire
        # length of the tree, for O(N) time complexity.

        # Make sure that q_node is the node with the highest level.
        if level[q_node] < level[p_node]:
            p_node, q_node = q_node, p_node

        # Move q_node up until it is at the same level as p_node.
        while level[q_node] > level[p_node]:
            q_node = parent[q_node]

        # Now that the nodes are at the same level, move them both up
        # until they are equal.
        while q_node != p_node:
            q_node = parent[q_node]
            p_node = parent[p_node]

        # Overall, this is a O(N) solution.
        return q_node
