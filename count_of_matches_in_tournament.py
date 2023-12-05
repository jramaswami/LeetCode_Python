"""
LeetCode
1688. Count of Matches in Tournament
December 2023
jramaswami
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        soln = 0
        while n > 1:
            n, r = divmod(n, 2)
            soln += n
            n += r
        return soln