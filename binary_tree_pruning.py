"""
LeetCode :: July 2021 Challenge :: Binary Tree Pruning
jramaswami
"""


class Solution:
    def pruneTree(self, root):

        def prune(node):
            if node is None:
                return None

            node.left = prune(node.left)
            node.right = prune(node.right)
            if node.left or node.right or node.val:
                return node
            else:
                return None

        return prune(root)
