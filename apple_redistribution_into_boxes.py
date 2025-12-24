"""
LeetCode
3074. Apple Redistribution into Boxes
December 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        soln = 0
        curr = sum(apple)
        i = 0
        while curr > 0:
            soln += 1
            curr -= capacity[i]
            i += 1
        return soln