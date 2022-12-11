"""
LeetCode
124. Binary Tree Maximum Path Sum
December 2022 Challenge
jramaswami
"""


import collections
import math


Result = collections.namedtuple('Result', ['max_leg', 'max_path'])


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            if node is None:
                return Result(-math.inf, -math.inf)

            left_result = traverse(node.left)
            right_result = traverse(node.right)
            my_max_leg = max(
                # Just me.
                node.val,
                # Me + the left leg.
                node.val + left_result.max_leg,
                # Me + the right leg.
                node.val + right_result.max_leg
            )
            my_max_path = max(
                # Just me.
                node.val,
                # The max path on the left.
                left_result.max_path,
                # The max path on the right.
                right_result.max_path,
                # My max leg.
                my_max_leg,
                # Me as the head of two legs.
                node.val + left_result.max_leg + right_result.max_leg
            )
            return Result(my_max_leg, my_max_path)

        return traverse(root).max_path
