"""
LeetCode :: December 2021 Challenge :: 337. House Robber III
jramaswami
"""


import functools


class Solution:

    def rob(self, root):

        @functools.cache
        def traverse(house, can_rob):
            if house is None:
                return 0

            # I can rob this house, but then I cannot rob direct children.
            rob_this_house = 0
            if can_rob:
                rob_this_house = (
                        house.val +
                        traverse(house.left, False) +
                        traverse(house.right, False)
                )
            # I can skip this house and rob the direct children.
            skip_this_house = (
                traverse(house.left, True) +
                traverse(house.right, True)
            )
            return max(rob_this_house, skip_this_house)

        return traverse(root, True)
