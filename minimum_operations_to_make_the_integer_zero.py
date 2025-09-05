"""
LeetCode
2749. Minimum Operations to Make the Integer Zero
September 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/2749
"""


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            x = num1 - (k * num2)
            if x > 0:
                bits = x.bit_count()
                if bits <= k <= x:
                    return k
        return -1