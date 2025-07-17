"""
LeetCode
3202. Find the Maximum Length of Valid Subsequence II
July 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        soln = 0
        # dp[i][x] = current length
        dp = [[0 for _ in range(k)] for _ in nums]
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                x = (a + b) % k
                if dp[i][x] == 0:
                    dp[j][x] = 2
                else:
                    dp[j][x] = 1 + dp[i][x]
                soln = max(soln, dp[j][x])
        return soln