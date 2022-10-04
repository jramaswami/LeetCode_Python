"""
LeetCode :: October 2022 Challenge :: 112. Path Sum
jramaswami
"""


class Solution:

    def hasPathSum(self, root, target_sum):
        def is_leaf(node):
            return node.left is None and node.right is None

        def rec(node, acc):
            if node is None:
                return False

            if is_leaf(node):
                return acc + node.val == target_sum

            return (
                rec(node.left, node.val + acc) or
                rec(node.right, node.val + acc)
            )

        return rec(root, 0)