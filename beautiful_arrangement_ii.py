"""
LeetCode :: April 2021 Challenge :: Beautiful Arrangement II
jramaswami
"""
from typing import *


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # First difference is 1
        k -= 1
        LEFT = 1
        RIGHT = -1
        m = 2
        soln = [1,]
        curr = LEFT
        for _ in range(n-1):
            if k:
                # Need to switch
                k -= 1
                if curr == LEFT:
                    curr = RIGHT
                    soln.append(n)
                    n -= 1
                else:
                    curr = LEFT
                    soln.append(m)
                    m += 1
            else:
                if curr == LEFT:
                    soln.append(m)
                    m += 1
                else:
                    soln.append(n)
                    n -= 1
        return soln


#
# Testing
#
import random


def verify(arr, n, k):
    """Verify that arrangement is beautiful."""
    return (sorted(arr) == list(range(1, n+1)) and
            len(set(abs(a - b) for a, b in zip(arr[:-1], arr[1:]))) == k)


def test_1():
    n = 3
    k = 1
    result = Solution().constructArray(n, k)
    print(result)
    assert verify(result, n, k)


def test_2():
    n = 3
    k = 2
    result = Solution().constructArray(n, k)
    print(result)
    assert verify(result, n, k)


def test_3():
    n = random.randint(5, 1000)
    k = random.randint(1, n-1)
    result = Solution().constructArray(n, k)
    assert verify(result, n, k)
