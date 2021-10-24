"""
LeetCode :: October 2021 Challenge :: 222. Count Complete Tree Nodes
jramaswami

Given that a complete tree has up to 2h nodes.

"""


import collections


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Corner case: null tree.
        if root is None:
            return 0

        # Get the height of the tree.  Since the last level
        # is filled from the left, just go left until there
        # are no more nodes.  This is done in O(H) timer where
        # H is the height of the tree.
        node = root
        height = 0
        while node:
            node = node.left
            height += 1

        # Compute the total number of possible nodes.
        node_count = pow(2, height) - 1

        # Use BFS to find the null nodes at the bottom.
        # Do not process the bottom row.
        queue = collections.deque()
        queue.append((root, 1))
        while queue:
            node, ht = queue.popleft()

            # Corner case: tree with height of one.
            if ht == height:
                break

            if node.left is None:
                node_count -= 1
            if node.right is None:
                node_count -= 1

            if ht + 1 < height and node.left:
                queue.append((node.left, ht + 1))
            if ht + 1 < height and node.right:
                queue.append((node.right, ht + 1))

        return node_count
