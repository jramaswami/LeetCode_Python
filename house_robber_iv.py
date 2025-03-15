"""
LeetCode
2560. House Robber IV
March 2025 Challenge
jramaswami
"""


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        INF = pow(10, 10)
        # dp[houses robbed: n][house index: i] = max value after robbing n houses at index i
        dp = [[INF for _ in nums] for _ in range(k+1)]
        dp[0] = [0 for _ in nums]
        dp[1] = list(nums)
        for n in range(1, k):
            for i in range(len(nums)):
                if dp[n][i] < INF:
                    # I have robbed this house
                    # I can rob another house and my capacity will be the min of this house
                    # and the next.  I want to record the minimum capacity to have robbed
                    # n+1 houses at house j.
                    for j in range(i+2, len(nums)):
                        dp[n+1][j] = min(dp[n+1][j], max(dp[n][i], nums[j]))
        return min(dp[-1])