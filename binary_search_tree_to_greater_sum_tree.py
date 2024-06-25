"""
LeetCode
1038. Binary Search Tree to Greater Sum Tree
June 2024 Challenge
jramaswami
"""


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def rec(node, above_right):
            if node is None:
                return 0, None

            below_right, new_right = rec(node.right, above_right)
            below_left, new_left = rec(node.left, above_right + below_right + node.val)
            new_node = TreeNode(node.val + above_right + below_right, new_left, new_right)
            return node.val + below_left + below_right, new_node

        return rec(root, 0)[1]