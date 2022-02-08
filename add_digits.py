"""
LeetCode :: February 2022 Challenge :: 258. Add Digits
jramaswami
"""


class Solution:
    def addDigits(self, num: int) -> int:
        def sum_digits(n):
            s = 0
            while n:
                n, r = divmod(n, 10)
                s += r
            return s

        while num >= 10:
            num = sum_digits(num)
        return num
