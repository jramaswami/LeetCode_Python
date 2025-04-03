"""
LeetCode
2874. Maximum Value of an Ordered Triplet II
April 2025 Challenge
jramaswami
"""


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        INF = pow(10, 10)
        prefix = [-INF for _ in nums]
        curr_max = -INF
        for i, n in enumerate(nums):
            curr_max = max(curr_max, n)
            prefix[i] = curr_max

        suffix = [-INF for _ in nums]
        curr_max = -INF
        for i in range(len(nums) - 1, -1, -1):
            curr_max = max(curr_max, nums[i])
            suffix[i] = curr_max

        soln = 0
        for j, y in enumerate(nums[1:-1], start=1):
            x = prefix[j-1]
            z = suffix[j+1]
            soln = max(soln, (x - y) * z)
        return soln