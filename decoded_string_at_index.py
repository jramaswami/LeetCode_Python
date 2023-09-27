"""
LeetCode
880. Decoded String at Index
September 2023 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=UgSrm6LwXqk
"""


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0

        for c in s:
            if c.isdigit():
                length = length * int(c)
            else:
                length += 1

        for c in reversed(s):
            if c.isdigit():
                length //= int(c)
                k %= length
            elif k == 0 or k == length:
                return c
            else:
                length -= 1


def test_1():
    s = "leet2code3"
    k = 10
    expected = "o"
    assert Solution().decodeAtIndex(s, k) == expected


def test_2():
    s = "ha22"
    k = 5
    expected = "h"
    assert Solution().decodeAtIndex(s, k) == expected


def test_3():
    s = "a2345678999999999999999"
    k = 1
    expected = "a"
    assert Solution().decodeAtIndex(s, k) == expected


