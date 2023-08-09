"""
LeetCode
2616. Minimize the Maximum Difference of Pairs
August 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def check(guess):
            i = 0
            p0 = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= guess:
                    p0 += 1
                    i = i + 2
                else:
                    i = i + 1
            return p0 >= p

        lo = 0
        hi = pow(10, 9)
        soln = hi
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                hi = mid - 1
                soln = min(soln, mid)
            else:
                lo = mid + 1
        return soln


def test_1():
    nums = [10,1,2,7,1,3]
    p = 2
    expected = 1
    assert Solution().minimizeMax(nums, p) == expected


def test_2():
    nums = [4,2,1,2]
    p = 1
    expected = 0
    assert Solution().minimizeMax(nums, p) == expected