"""
LeetCode :: 938. Range Sum of BST
December 2022 Challenge
jramaswami
"""


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def traverse(node, lo, hi):
            if node is None:
                return 0

            if lo <= node.val <= hi:
                return (
                    node.val +
                    traverse(node.left, lo, hi) +
                    traverse(node.right, lo, hi)
                )
            elif node.val < lo:
                return traverse(node.right, lo, hi)
            elif node.val > hi:
                return traverse(node.left, lo, hi)

        return traverse(root, low, high)
