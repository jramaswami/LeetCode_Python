"""
LeetCode
1262. Greatest Sum Divisible by Three
November 2025 Challenge
jramaswami
"""


import heapq
import math
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        S = sum(nums)
        ones = heapq.nsmallest(2, (n for n in nums if n % 3 == 1))
        twos = heapq.nsmallest(2, (n for n in nums if n % 3 == 2))
        print(ones, twos)
        r = S % 3
        x = 0
        if r == 1:
            x = min(math.inf if not ones else ones[0], math.inf if len(twos) < 2 else sum(twos))
        elif r == 2:
            x = min(math.inf if len(ones) < 2 else sum(ones), math.inf if not twos else twos[0])
        return max(S - x, 0)