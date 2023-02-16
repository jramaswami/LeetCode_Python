"""
LeetCode
104. Maximum Depth of Binary Tree
February 2023 Challenge
jramaswami
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            if node is None:
                return 0
            return 1 + max(traverse(node.left), traverse(node.right))

        return traverse(root)