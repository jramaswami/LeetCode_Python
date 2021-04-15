"""
LeetCode :: April 2021 Challenge :: Fibonacci Numbers
jramaswami
"""
from functools import lru_cache
from typing import *


@lru_cache(maxsize=None)
def fib0(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib0(n-1) + fib0(n-2)


class Solution:
    def fib(self, n: int) -> int:
        return fib0(n)


def test_1():
    assert Solution().fib(2) == 1

def test_2():
    assert Solution().fib(3) == 2

def test_3():
    assert Solution().fib(4) == 3
