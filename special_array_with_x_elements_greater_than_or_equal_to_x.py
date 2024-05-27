"""
LeetCode
1608. Special Array With X Elements Greater Than or Equal X
May 2024 Challenge
jramaswami
"""


import bisect
from typing import List


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(1, len(nums)+1):
            try:
                i = find_ge(nums, x)
                if len(nums) - i== x:
                    return x
            except:
                pass
        return -1


def test_1():
    nums = [3,5]
    expected = 2
    assert Solution().specialArray(nums) == expected


def test_2():
    nums = [0,0]
    expected = -1
    assert Solution().specialArray(nums) == expected


def test_3():
    nums = [0,4,3,0,4]
    expected = 3
    assert Solution().specialArray(nums) == expected