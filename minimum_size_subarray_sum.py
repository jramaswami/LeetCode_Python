"""
LeetCode
209. Minimum Size Subarray Sum
July 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = 10**20
        window = collections.deque()
        curr_sum = 0
        soln = INF
        for n in nums:
            window.append(n)
            curr_sum += n
            while curr_sum >= target:
                soln = min(soln, len(window))
                curr_sum -= window[0]
                window.popleft()
        if soln == INF:
            return 0
        return soln