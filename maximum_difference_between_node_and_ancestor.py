"""
LeetCode :: December 2021 Challenge :: 1026. Maximum Difference Between Node and Ancestor
jramaswami
"""


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def traverse(node, max_val, min_val):
            if node is None:
                return max_val - min_val

            left_val = traverse(
                node.left,
                max(node.val, max_val),
                min(node.val, min_val)
            )

            right_val = traverse(
                node.right,
                max(node.val, max_val),
                min(node.val, min_val)
            )

            return max(left_val, right_val)

        return traverse(root, root.val, root.val)

