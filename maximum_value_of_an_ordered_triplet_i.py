"""
LeetCode
2873. Maximum Value of an Ordered Triplet I
April 2025 Challenge
jramaswami
"""


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Do one pass to find the largest number to the right
        INF = pow(10, 10)
        suffix = [-INF for _ in nums]
        curr_max = -INF
        for i in range(len(nums) - 1, -1, -1):
            curr_max = max(curr_max, nums[i])
            suffix[i] = curr_max
        # o(n^2) to find soln
        soln = 0
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:-1], start=i+1):
                z = suffix[j+1]
                soln = max(soln, (x - y) * z)
        return soln