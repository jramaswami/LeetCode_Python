"""
Leet Code :: April 2021 Challenge :: Brick Wall
jramaswami
"""
from typing import *
from collections import Counter
from itertools import accumulate


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        frequencies = Counter()
        for row in wall:
            frequencies.update(accumulate(row))
        if len(frequencies) > 1:
            return len(wall) - frequencies.most_common(2)[1][1]
        return len(wall)


def test_1():
    wall = [[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1]]
    assert Solution().leastBricks(wall) == 2

def test_2():
    wall = [[1],[1],[1]]
    assert Solution().leastBricks(wall) == 3
