"""
LeetCode :: September 2022 Challenge :: 1680. Concatenation of Consecutive Binary Numbers
jramaswami
"""


import math
import collections


CacheItem = collections.namedtuple('CacheItem', ['value', 'bit_length'])


class Solution:

    def __init__(self):
        # Cache results.
        pows2 = [CacheItem(pow(2, i), i) for i in range(19)][::-1]
        MOD = pow(10, 9) + 7
        self.cache = [CacheItem(0, 0)]
        limit = pow(10,5)
        for x in range(1, limit+1):
            while x >= pows2[-1].value:
                pows2.pop()
            # Take previous value and shift it by the current values
            # number of pits.
            p = pow(2, pows2[-1].bit_length, MOD)
            t = (self.cache[-1].value * p) % MOD
            # Add current value.
            y = (x + t) % MOD
            # Figure out how many bits we no have.
            l = pows2[-1].bit_length + self.cache[-1].bit_length
            self.cache.append(CacheItem(y, l))

    def concatenatedBinary(self, n: int) -> int:
        return self.cache[n].value


def test_1():
    n = 1
    expected = 1
    assert Solution().concatenatedBinary(n) == expected


def test_2():
    n = 3
    expected = 27
    assert Solution().concatenatedBinary(n) == expected


def test_3():
    n = 12
    expected = 505379714
    assert Solution().concatenatedBinary(n) == expected


def test_4():
    "TLE on 354/403 testcase."
    n = 95830
    expected = 664636239
    assert Solution().concatenatedBinary(n) == expected