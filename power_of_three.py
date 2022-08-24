"""
Leet Code :: August 2022 Challenge :: Power of Three
jramaswami
"""


class Solution:
    def __init__(self):
        # Cache the largest power of three more than the limit of 2^32.
        # This number will be divisible evenly by any other power of three
        # less thatn 2^32.
        self.T = 1
        L = pow(2, 32)
        while self.T < L:
            self.T *= 3

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and self.T % n == 0


def test_1():
    "WA"
    assert Solution().isPowerOfThree(243) == True


def test_2():
    "WA"
    assert Solution().isPowerOfThree(45) == False