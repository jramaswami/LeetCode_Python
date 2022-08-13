"""
LeetCode :: 1884. Egg Drop With 2 Eggs and N Floors
jramaswami

Thank You Larry!
"""


import math


class Solution:

    def twoEggDrop(self, n: int) -> int:
        # Binary search the answer.

        def check(x):
            return (x * (x + 1)) // 2 >= n

        lo = 0
        hi = n
        soln = n
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                soln = min(mid, soln)
                hi = mid - 1
            else:
                lo = mid + 1
        return soln



def test_1():
    n = 2
    expected = 2
    assert Solution().twoEggDrop(n) == expected


def test_2():
    n = 100
    expected = 14
    assert Solution().twoEggDrop(n) == expected