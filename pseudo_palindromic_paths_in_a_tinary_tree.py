"""
LeetCode :: September 2022 Challenge :: Pseudo-Palindromic Paths in a Binary Tree
jramaswami
"""


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def is_leaf(node):
            "Return True if node is a leaf node."
            return node.left is None and node.right is None

        def is_palindromic(acc):
            "Return 1 if acc is palindromic."
            count_odds = sum(t % 2 for t in acc)
            return 1 if count_odds <= 1 else 0

        def rec(node, acc):
            if node is None:
                return 0

            acc[node.val] += 1
            if is_leaf(node):
                return is_palindromic(acc)

            return (
                rec(node.left, list(acc)) +
                rec(node.right, list(acc))
            )

        return rec(root, [0 for _ in range(10)])