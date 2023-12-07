"""
LeetCode
1903. Largest Odd Number in String
December 2023 Challenge
jramaswami
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0:
            if int(num[i]) % 2:
                break
            i-= 1
        return num[:i+1]