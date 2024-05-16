"""
LeetCode
2331. Evaluate Boolean Binary Tree
May 2024 Challenge
jramaswami
"""


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def is_leaf(node):
            return node.left is None and node.right is None

        def rec(node):
            if is_leaf(node):
                return True if node.val == 1 else False

            if node.val == 2:
                return rec(node.left) or rec(node.right)
            elif node.val == 3:
                return rec(node.left) and rec(node.right)

        return rec(root)