"""
LeetCode :: October 2021 Challenge :: 226. Invert Binary Tree
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
