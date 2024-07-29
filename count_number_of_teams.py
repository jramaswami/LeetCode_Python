"""
LeetCode
1395. Count Number of Teams
July 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        soln = 0
        for i, n in enumerate(rating):
            left_less_than = sum(1 for x in rating[:i] if x < n)
            right_greater_than = sum(1 for x in rating[i+1:] if x > n)
            soln += (left_less_than * right_greater_than)

            left_greater_than = i - left_less_than
            right_less_than = len(rating) - i - 1 - right_greater_than
            soln += (left_greater_than * right_less_than)
        return soln