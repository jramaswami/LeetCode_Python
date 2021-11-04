"""
LeetCode :: November 2021 Challenge :: 404. Sum of Left Leaves
jramaswami

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def is_leaf(node):
            return node.left is None and node.right is None

        def traverse(node, is_left):
            if node is None:
                return 0

            if is_leaf(node) and is_left:
                return node.val

            return traverse(node.left, True) + traverse(node.right, False)

        return traverse(root, False)