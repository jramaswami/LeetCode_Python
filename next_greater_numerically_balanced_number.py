"""
LeetCode
2048. Next Greater Numerically Balanced Number
October 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x):
            freqs = collections.Counter(str(x))
            for digit, freq in freqs.items():
                if int(digit) != freq:
                    return False
            return True

        soln = n + 1
        while not is_balanced(soln):
            soln += 1
        return soln