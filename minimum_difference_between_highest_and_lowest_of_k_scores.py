"""
LeetCode
1984. Minimum Difference Between Highest and Lowest of K Scores
January 2026 Challenge
jramaswami
"""


import collections


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        window = collections.deque(nums[:k])
        soln = window[-1] - window[0]
        for n in nums[k:]:
            window.popleft()
            window.append(n)
            soln = min(soln, window[-1] - window[0])
        return soln
