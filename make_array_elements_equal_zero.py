"""
LeetCode
3354. Make Array Elements Equal to Zero
October 2025 Challenge
jramaswami

For any given 0, if the prefix sum and suffix sum are equal
then you can go either direction.  If the difference is one,
than you can go toward the greater value.  Otherwise, there
is no valid move.
"""


from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix = []
        curr = 0
        for n in nums:
            prefix.append(curr)
            curr += n
        suffix = []
        curr = 0
        for n in reversed(nums):
            suffix.append(curr)
            curr += n
        suffix = suffix[::-1]
        soln = 0
        for i, n in enumerate(nums):
            if n == 0:
                if prefix[i] == suffix[i]:
                    soln += 2
                elif abs(prefix[i] - suffix[i]) == 1:
                    soln += 1
        return soln