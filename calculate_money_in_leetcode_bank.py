"""
LeetCode
1716. Calculate Money in Leetcode Bank
December 2023 Challenge
jramaswami
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        curr = 1
        start = 1
        soln = 0
        for x in range(1, n+1):
            soln += curr
            curr += 1
            if x % 7 == 0:
                start += 1
                curr = start
        return soln