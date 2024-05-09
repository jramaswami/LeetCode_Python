"""
LeetCode
3075. Maximize Happiness of Selected Children
jramaswami
"""


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        soln = 0
        happiness.sort(reverse=True)
        for i, h in enumerate(happiness[:k]):
            soln = max(soln, soln + (h - i))
        return soln