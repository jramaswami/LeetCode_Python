"""
LeetCode :: November Challenge :: 129. Sum Root to Leaf Numbers
jramaswami

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def sumNumbers(self, root):

        def traverse(node, acc):
            if node is None:
                return 0

            acc0 = (10 * acc) + node.val

            # Leaf node
            if node.left is None and node.right is None:
                return acc0

            return traverse(node.left, acc0) + traverse(node.right, acc0)

        return traverse(root, 0)