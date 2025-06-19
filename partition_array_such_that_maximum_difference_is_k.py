"""
LeetCode
2294. Partition Array Such That Maximum Difference Is K
June 2025 Challenge
jramaswami
"""


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        soln = 0
        curr_min = nums[0]
        for n in nums:
            if n - curr_min > k:
                soln += 1
                curr_min = n
        soln += 1
        return soln