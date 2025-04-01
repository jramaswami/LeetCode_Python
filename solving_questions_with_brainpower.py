"""
LeetCode
2140. Solving Questions With Brainpower
April 2025 Challenge
jramaswami
"""


from typing import List
import functools


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @functools.cache
        def rec(i):
            if i >= len(questions):
                return 0

            points, brainpower = questions[i]
            return max(points + rec(i+brainpower+1), rec(i+1))
        return rec(0)