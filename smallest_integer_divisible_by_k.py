"""
LeetCode :: December 2021 Challenge :: 1015. Smallest Integer Divisible by K
jramaswami

Thank You Larry!
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Numbers divisible by 2 or 5 will never have product with all ones.
        if k % 2 == 0 or k % 5 == 0:
            return -1

        r = 0
        for soln in range(1, k+1):
            r = (r * 10 + 1) % k
            if r == 0:
                return soln
        return -1


def test_1():
    k = 1
    assert Solution().smallestRepunitDivByK(k) == 1


def test_2():
    k = 2
    assert Solution().smallestRepunitDivByK(k) == -1


def test_3():
    k = 3
    assert Solution().smallestRepunitDivByK(k) == 3


def test_4():
    "TLE: endless loop?"
    k = 19927
    assert Solution().smallestRepunitDivByK(k) == 19926
