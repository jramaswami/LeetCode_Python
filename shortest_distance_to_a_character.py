"""
LeetCode :: Shortest Distance to a Character
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prefix = [inf for _ in s]
        suffix = [inf for _ in s]

        acc = inf
        for i, a in enumerate(s):
            if a == c:
                acc = 0
            else:
                acc += 1
            prefix[i] = acc

        acc = inf
        for i, a in enumerate(reversed(s), start=-(len(s) - 1)):
            if a == c:
                acc = 0
            else:
                acc += 1
            suffix[abs(i)] = acc

        return [min(a, b) for a, b in zip(prefix, suffix)]


def test_1():
    assert Solution().shortestToChar('loveleetcode', 'e') == [3,2,1,0,1,0,0,1,2,2,1,0]

def test_2():
    assert Solution().shortestToChar('aaab', 'b') == [3, 2, 1, 0]
