"""
LeetCode
1422. Maximum Score After Splitting a String
December 2023 Challenge
jramaswami
"""


class Solution:
    def maxScore(self, s: str) -> int:
        curr_ones = s.count('1')
        curr_zeros = 0
        soln = 0
        for n in s[:-1]:
            if n == '1':
                curr_ones -= 1
            elif n == '0':
                curr_zeros += 1
            soln = max(soln, curr_zeros + curr_ones)
        return soln