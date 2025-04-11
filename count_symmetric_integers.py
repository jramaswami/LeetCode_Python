"""
LeetCode
2843. Count Symmetric Integers
April 2025 Challenge
jramaswami
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def digit_sum(s):
            return sum(int(t) for t in s)

        def is_symmetric(n):
            s = str(n)
            if len(s) % 2:
                return False
            mid = len(s) // 2
            return digit_sum(s[:mid]) == digit_sum(s[mid:])

        return sum(1 if is_symmetric(n) else 0 for n in range(low, high+1))