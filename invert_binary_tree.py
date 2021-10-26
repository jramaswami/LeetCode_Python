"""
LeetCode :: October 2021 Challenge :: 226. Invert Binary Tree
jramaswami
"""


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def invert(node):
            if node:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)

        invert(root)
        return root
