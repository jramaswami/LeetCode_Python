"""
LeetCode :: The K Weakest Rows in a Matrix
jramaswami
"""
from typing import *
from itertools import islice


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for _, i in islice(sorted((sum(row), i) for i, row in enumerate(mat)), k)]


def test_1():
    mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
    k = 3
    assert Solution().kWeakestRows(mat, k) == [2, 0, 3]


def test_2():
    mat = [[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]]
    k = 2
    assert Solution().kWeakestRows(mat, k) == [0, 2]
