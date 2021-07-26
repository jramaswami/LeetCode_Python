"""
LeetCode :: July 2021 Challenge :: Convert Sorted Array to Binary Search Tree
jramaswami
"""


class Solution:
    def sortedArrayToBST(self, nums):

        def build_bst(lo, hi):
            """Build the binary search tree."""
            if lo > hi:
                return None

            mid = lo + ((hi - lo) // 2)
            node = TreeNode(nums[mid])
            node.left = bst(lo, mid - 1)
            node.right = bst(mid + 1, hi)
            return node

        return build_bst(0, len(nums) - 1)
