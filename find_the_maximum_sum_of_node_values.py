"""
LeetCode
3068. Find the Maximum Sum of Node Values
May 2024 Challenge
jramaswami

Thank You Larry!
"""


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        deltas = [(x^k) - x for x in nums]
        deltas.sort(reverse=True)
        soln = curr_total = sum(nums)
        for i in range(0, len(deltas)-1, 2):
            curr_total += deltas[i]
            curr_total += deltas[i+1]
            soln = max(soln, curr_total)
        return soln