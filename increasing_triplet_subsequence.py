"""
LeetCode :: October 2022 Challenge :: 334. Increasing Triplet Subsequence
jramaswami
"""


from typing import *
import bisect


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lis = []
        for n in nums:
            if (not lis) or (lis[-1] < n):
                lis.append(n)
            else:
                i = bisect.bisect_left(lis, n)
                lis[i] = n
        return len(lis) >= 3


def test_1():
    nums = [1,2,3,4,5]
    expected = True
    assert Solution().increasingTriplet(nums) == expected


def test_2():
    nums = [5,4,3,2,1]
    expected = False
    assert Solution().increasingTriplet(nums) == expected


def test_3():
    nums = [2,1,5,0,4,6]
    expected = True
    assert Solution().increasingTriplet(nums) == expected