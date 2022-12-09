"""
LeetCode
1026. Maximum Difference Between Node and Ancestor
December 2022 Challenge
jramaswami
"""


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            "Return min_child, max_child, max_result"
            if node is None:
                return math.inf, -math.inf, 0

            left_min, left_max, left_result = traverse(node.left)
            right_min, right_max, right_result = traverse(node.right)

            my_min = min(left_min, right_min, node.val)
            my_max = max(left_max, right_max, node.val)
            my_result = max(
                left_result, right_result,
                abs(node.val - my_min), abs(node.val - my_max)
            )

            return my_min, my_max, my_result

        return traverse(root)[2]