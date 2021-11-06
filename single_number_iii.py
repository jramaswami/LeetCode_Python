"""
LeetCode :: November 2021 Challenge :: 260. Single Number III
"""


class Solution:
    def singleNumber(self, nums):
        # Per Python Wiki set operations are O(1) amortized.
        # So at most we will add each item once and remove
        # all but two items once: 2 * O(N) = O(N).
        visited = set()
        for n in nums:
            if n in visited:
                visited.remove(n)
            else:
                visited.add(n)
        return list(visited)