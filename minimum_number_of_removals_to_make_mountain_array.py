"""
LeetCode
1671. Minimum Number of Removals to Make Mountain Array
October 2024 Challenge
jramaswami

Thank You NeetCode.IO
"""


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        increasing_dp = [1 for _ in nums]
        for right in range(len(nums)):
            for left in range(right):
                if nums[left] < nums[right]:
                    increasing_dp[right] = max(increasing_dp[left]+1, increasing_dp[right])
        
        decreasing_dp = [1 for _ in nums]
        for left in range(len(nums)-1, -1, -1):
            for right in range(left+1, len(nums)):
                if nums[left] > nums[right]:
                    decreasing_dp[left] = max(decreasing_dp[left], decreasing_dp[right]+1)

        soln = pow(10, 10)
        for i in range(1, len(nums)-1):
            if increasing_dp[i] > 1 and decreasing_dp[i] > 1:
                x = increasing_dp[i] + decreasing_dp[i] - 1
                soln = min(soln, len(nums)-x)
        return soln
