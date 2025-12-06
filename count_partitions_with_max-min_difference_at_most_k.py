"""
LeetCode
578. Count Partitions With Max-Min Difference at Most K
December 2025 Challenge
jramawami

REF: https://algo.monster/liteproblems/3578
"""


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = pow(10, 9) + 7
        sorted_window = SortedList()
        # dp[i] = number of ways to partition nums[0:i]
        dp = [1] + [0] * len(nums)
        # prefix_sum[i] = sum(dp[0:i])
        prefix_sum = [1] + [0] * len(nums)
        # Sliding window
        left = 1
        for right, val in enumerate(nums, start=1):
            sorted_window.add(val)
            # Invariant: window should have maximum difference of k
            while sorted_window[-1] - sorted_window[0] > k:
                sorted_window.remove(nums[left - 1])
                left += 1
            if left >= 2:
                dp[right] = prefix_sum[right - 1] - prefix_sum[left - 2]
                dp[right] += MOD  # Prevent negative numbers
                dp[right] %= MOD
            else:
                dp[right] = prefix_sum[right - 1] % MOD
            prefix_sum[right] = prefix_sum[right - 1] + dp[right]
            prefix_sum[right] %= MOD
        return dp[-1]