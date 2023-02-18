"""
LeetCode
226. Invert Binary Tree
February 2023 Challenge
jramaswami
"""


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def invert(node):
            if node:
                return TreeNode(
                    node.val,
                    invert(node.right),
                    invert(node.left)
                )
            else:
                return None

        return invert(root)
