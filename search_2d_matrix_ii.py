"""
LeetCode :: Search a 2D Matrix II
jramaswami
"""
from typing import *
from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                i = bisect_left(row, target)
                if i < len(row) and row[i] == target:
                    return True
        return False

def test_1():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    assert Solution().searchMatrix(matrix, target) == True

def test_2():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    assert Solution().searchMatrix(matrix, target) == False

