"""
LeetCode :: October 2022 Challenge :: 976. Largest Perimeter Triangle
jramaswami
"""


from typing import *


class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        a, b, c = nums
        if b + c <= a:
            return 0
        elif a + c <= b:
            return 0
        elif a + b <= c:
            return 0
        return a + b + c


def test_1():
    nums = [2,1,2]
    expected = 5
    assert Solution().largestPerimeter(nums) == expected


def test_2():
    nums = [1,2,1]
    expected = 0
    assert Solution().largestPerimeter(nums) == expected


def test_3():
    "RTE. Made assumption there were three sides only, but there can be more."
    nums = [3,2,3,4]
    expected = -1
    assert Solution.largestPerimeter(nums) == expected