"""
LeetCode :: January 2022 Challenge :: 1022. Sum of Root To Leaf Binary Numbers
jramaswami
"""


class Solution:
    def sumRootToLeaf(self, root):

        def is_leaf(node):
            return node.left is None and node.right is None

        def traverse(node, acc):
            acc0 = (acc * 2) + node.val

            if is_leaf(node):
                return acc0

            result = 0
            if node.left:
                result += traverse(node.left, acc0)
            if node.right:
                result += traverse(node.right, acc0)
            return result

        return traverse(root, 0)
