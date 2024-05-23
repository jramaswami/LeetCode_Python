"""
LeetCode
2597. The Number of Beautiful Subsets
May 2024 Challenge
jramaswami
"""


import bisect
from typing import List


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()

        def rec(i, acc):
            if i >= len(nums):
                if acc:
                    return 1
                return 0
            else:
                result = 0
                # Without me
                result += rec(i+1, acc)
                # With me
                x = nums[i]
                if index(acc, x - k) == -1:
                    acc.append(x)
                    result += rec(i+1, acc)
                    acc.pop()
                return result

        return rec(0, [])


def test_1():
    nums = [2,4,6]
    k = 2
    expected = 4
    result = Solution().beautifulSubsets(nums, k)
    assert result == expected