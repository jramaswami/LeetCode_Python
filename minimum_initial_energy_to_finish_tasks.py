"""
LeetCode
1665. Minimum Initial Energy to Finish Tasks
May 2026 Challenge
jramaswami

REF: https://algo.monster/liteproblems/1665
"""


from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[0] - t[1])
        soln = 0
        curr = 0
        for ac, mn in tasks:
            if curr < mn:
                soln += (mn - curr)
                curr = mn
            curr -= ac
        return soln