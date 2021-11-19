"""
LeetCode :: November 2021 Challenge :: 461. Hamming Distance
jramswami
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        def popcount(n):
            bits = 0
            while n:
                if n & 1:
                    bits += 1
                n >>= 1
            return bits

        return popcount(x ^ y)


def test_1():
    assert Solution().hammingDistance(3, 1) == 1