"""
LeetCode :: August 2022 Challenge :: Convert Sorted Array to Binary Search Tree
jramaswami
"""


class Solution:
    def sortedArrayToBST(self, nums):

        def build(A):
            if len(A) == 0:
                return None
            if len(A) == 1:
                return TreeNode(A[0])

            mid = 1 + (len(A) // 2)
            return TreeNode(
                A[mid],
                build(A[:mid]),
                build(A[mid+1:])
            )

        return build(nums)
