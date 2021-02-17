"""
LeetCode :: Container With Most Water
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Make an array of the largest item to the left, include index.
        prefix_maxes = [-inf for _ in height]
        curr_max = (-inf, 0)
        for i, ht in enumerate(height):
            if ht > curr_max[0]:
                curr_max = (ht, i)
            prefix_maxes[i] = curr_max

        soln = -inf

        # For each index and height
        for i, ht in enumerate(height):
            # Find the height farthest to the left that is greater than or
            # equal to the current height.
            low = 0
            high = i - 1
            left = inf
            while low <= high:
                mid = low + ((high - low) // 2)
                if prefix_maxes[mid][0] >= ht:
                    left = min(left, prefix_maxes[mid][1])
                    high = mid - 1
                else:
                    low = mid + 1

            # Determine the max area possible from this height.
            if left != inf:
                soln = max(soln, (i - left) * ht)

        return soln



def test_1():
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49


def test_2():
    assert Solution().maxArea([1,1]) == 1


def test_3():
    assert Solution().maxArea([4,3,2,1,4]) == 16


def test_4():
    assert Solution().maxArea([1,2,1]) == 2

def test_5():
    assert Solution().maxArea([1,2]) == 1
