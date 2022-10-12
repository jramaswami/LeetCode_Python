"""
LeetCode :: October 2022 Challenge :: 976. Largest Perimeter Triangle
jramaswami
"""


from typing import *


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        soln = 0
        nums.sort()
        for i, _ in enumerate(nums[:-2]):
            a, b, c = nums[i:i+3]
            if abs(a - b) < c < a + b:
                soln = max(soln, a + b + c)
        return soln



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
    expected = 10
    assert Solution().largestPerimeter(nums) == expected