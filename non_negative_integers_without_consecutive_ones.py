"""
LeetCode :: July 2021 Challenge :: Non-negative Integers without Consecutive Ones
jramaswami
"""


from collections import deque
from bisect import bisect_right


NUMBERS = [0, 1]


def cache_numbers():
    # Cache the numbers.
    LIMIT = pow(10, 9)
    queue = deque([2])   # start with 2 (b10)
    while queue:
        k = queue.popleft()
        NUMBERS.append(k)
        k0 = k << 1
        k1 = 1 | (k << 1)
        if k & 1:
            # If k ends in a 1 then we must append a 0.
            if k0 <= LIMIT:
                queue.append(k0)
        else:
            # If k ends in a 0 then we can append a 0 or a 1.
            if k0 <= LIMIT:
                queue.append(k0)
            if k1 <= LIMIT:
                queue.append(k1)


cache_numbers()


class Solution:
    def findIntegers(self, n):
        return bisect_right(NUMBERS, n)


def test_1():
    assert Solution().findIntegers(5) == 5


def test_2():
    assert Solution().findIntegers(1) == 2


def test_3():
    assert Solution().findIntegers(2) == 3


def test_4():
    assert Solution().findIntegers(2) == 3


def test_5():
    assert Solution().findIntegers(9865786) == 103682


def test_6():
    """WA"""
    assert Solution().findIntegers(3) == 3

