"""
LeetCode :: December 2021 Challenge :: 337. House Robber III
jramaswami
"""


class Solution:

    def rob(self, root):
        even_nodes = []
        odd_nodes = []

        def traverse(node, level):
            if node:
                if level % 2:
                    odd_nodes.append(node.val)
                else:
                    even_nodes.append(node.val)
                traverse(node.left, level + 1)
                traverse(node.right, level + 1)

        traverse(root, 0)

        return max(
                sum(even_nodes) if even_nodes else 0,
                sum(odd_nodes) if odd_nodes else 0
        )
