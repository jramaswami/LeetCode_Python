"""
LeetCode
2999. Count the Number of Powerful Integers
April 2025 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=mhm9wbPKCEk
"""


import functools


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def cal(x, s, limit):
            """Return number of powerful numbers from 1 to x"""
            if len(x) < len(s):
                return 0
            if len(x) == len(s):
                return 0 if x < s else 1

            count = 0
            plen = len(x) - len(s)
            suffix = x[plen:]

            for i in range(plen):
                if int(x[i]) > limit:
                    count = count + (limit + 1) ** (plen - i)
                    return count
                count = count + int(x[i]) * (limit + 1) ** (plen - i - 1)

            if suffix >= s:
                count = count + 1

            return count

        return cal(str(finish), s, limit) - cal(str(start-1), s, limit)


def test_1():
    start = 1
    finish = 6000
    limit = 4
    s = "124"
    expected = 5