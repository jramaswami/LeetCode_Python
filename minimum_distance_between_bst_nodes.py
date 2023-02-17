"""
LeetCode
783. Minimum Distance Between BST Nodes
February 2023 Challenge
jramaswami
"""


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []

        def rec(node):
            if node is None:
                return
            rec(node.left)
            values.append(node.val)
            rec(node.right)

        rec(root)
        return min(abs(a-b) for a, b in zip(values[:-1], values[1:]))