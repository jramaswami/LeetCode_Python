"""
LeetCode :: April 2021 Challenge :: Minimum Operations to Make Array Equal
jramaswami
"""
import math


def solve(n):
    """Compute solution by simulating array."""
    soln = 0
    left = 1
    right = (2 * (n - 1)) + 1
    while left < right:
        soln += ((right - left) // 2)
        left += 2
        right -= 2
    return soln


def solve0(n):
    """
    OEIS A002620
    """
    return int(math.floor(n / 2) * math.ceil(n / 2))


class Solution:
    def minOperations(self, n: int) -> int:
        return solve0(n)


def test_1():
    assert Solution().minOperations(3) == 2

def test_2():
    assert Solution().minOperations(6) == 9

def test_3():
    assert Solution().minOperations(862) == 185761
