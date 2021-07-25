"""
LeetCode :: July 2021 Challenge :: Non-negative Integers without Consecutive Ones
jramaswami
"""


class Solution:
    def findIntegers(self, n):
        """Brute force."""

        def valid(k):
            prev = 0
            while k:
                curr = k & 1
                if prev & curr:
                    return False
                prev = curr
                k = k >> 1
            return True

        return sum(valid(i) for i in range(n+1))


def test_1():
    assert Solution().findIntegers(5) == 5


def test_2():
    assert Solution().findIntegers(1) == 2


def test_3():
    assert Solution().findIntegers(2) == 3
