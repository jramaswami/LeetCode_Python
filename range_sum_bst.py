"""
LeetCode :: December 2021 Challenge :: 938. Range Sum of BST
jramaswami
"""


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def traverse(node, lo, hi):
            if node is None:
                return 0

            if lo <= node.val <= hi:
                return node.val + traverse(node.left, lo, hi) + traverse(node.right, lo, hi)
            else:
                return traverse(node.left, lo, hi) + traverse(node.right, lo, hi)

        return traverse(root, low, high)
