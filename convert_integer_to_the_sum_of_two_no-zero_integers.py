"""
LeetCode
1317. Convert Integer to the Sum of Two No-Zero Integers
September 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def contains_zero(x):
            return any(t == '0' for t in str(x))

        for a in range(n):
            b = n - a
            if not contains_zero(a) and not contains_zero(b):
                return [a, b]
        return []
