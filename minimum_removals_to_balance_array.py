"""
LeetCode
3634. Minimum Removals to Balance Array
February 2026 Challenge
jramaswami
"""


from sortedcontainers import SortedList


class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        soln = 0
        S = SortedList(nums)
        for min_n in nums:
            max_n = k * min_n
            left = S.bisect_left(min_n)
            right = S.bisect_right(max_n)
            soln = max(soln, right - left)
        return len(nums) - soln