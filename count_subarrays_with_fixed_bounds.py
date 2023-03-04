"""
LeetCode
2444. Count Subarrays With Fixed Bounds
March 2023 Challenge
jramaswami
"""


import math
from typing import*


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        def check(window):
            if not window:
                return 0
            leftmost_max = [math.inf for _ in window]
            leftmost_min = [math.inf for _ in window]
            if window[-1] == minK:
                leftmost_min[-1] = len(window) - 1
            if window[-1] == maxK:
                leftmost_max[-1] = len(window) - 1
            for i in range(len(window) - 2, -1, -1):
                leftmost_min[i] = leftmost_min[i+1]
                if window[i] == minK:
                    leftmost_min[i] = i
                leftmost_max[i] = leftmost_max[i+1]
                if window[i] == maxK:
                    leftmost_max[i] = i

            result = 0
            for i, _ in enumerate(window):
                # I must have both min k and max k.
                must_go_to = max(leftmost_min[i], leftmost_max[i])
                if must_go_to < math.inf:
                    result += len(window) - must_go_to
            return result

        soln = 0
        window = []
        for n in nums:
            if minK <= n <= maxK:
                window.append(n)
            else:
                soln += check(window)
                window = []
        soln += check(window)
        return soln


def test_1():
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    expected = 2
    assert Solution().countSubarrays(nums, minK, maxK) == expected


def test_2():
    nums = [1,1,1,1]
    minK = 1
    maxK = 1
    expected = 10
    assert Solution().countSubarrays(nums, minK, maxK) == expected


def test_3():
    "RTE"
    nums = [934372,927845,479424,49441,17167,17167,65553,927845,17167,927845,17167,425106,17167,927845,17167,927845,251338,17167]
    minK = 17167
    maxK = 927845
    expected = 0
    assert Solution().countSubarrays(nums, minK, maxK) == expected