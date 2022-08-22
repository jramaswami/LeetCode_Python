"""
LeetCode :: August 2022 Challenge :: 342. Power of Four
jramaswami
"""

class Solution:

    def __init__(self):
        self.cache = set()
        curr = 1
        limit = pow(2, 32)
        while curr < limit:
            self.cache.add(curr)
            curr *= 4

    def isPowerOfFour(self, n: int) -> bool:
        print(self.cache)
        return abs(n) in self.cache


def test_1():
    assert Solution().isPowerOfFour(4) == True


def test_2():
    assert Solution().isPowerOfFour(5) == False


def test_3():
    assert Solution().isPowerOfFour(1) == True


def test_4():
    "WA"
    assert Solution().isPowerOfFour(-64) == False