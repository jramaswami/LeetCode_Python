"""
LeetCode :: October 2021 Challenge :: 1008. Construct Binary Search Tree from Preorder Traversal
"""
from leetcode_bst import TreeNode


class Solution:
    def bstFromPreorder(self, preorder):

        def solve(arr):
            if len(arr) == 0:
                return None

            # The root of the subtree is the first item in arr.
            root = TreeNode(arr[0])

            # All item less than root value go left.
            root.left = solve([k for k in arr if k < root.val])
            # All item more than root value go right.
            root.right = solve([k for k in arr if k > root.val])

            return root

        return solve(preorder)
