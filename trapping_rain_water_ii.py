"""
LeetCode
407. Trapping Rain Water II
January 2025 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        row_prefixes = []
        row_suffixes = []
        for row in height_map:
            row_prefixes.append([])
            curr_max = 0
            for x in row:
                curr_max = max(curr_max, x)
                row_prefixes[-1].append(curr_max)

            row_suffixes.append([])
            curr_max = 0
            for x in reversed(row):
                curr_max = max(curr_max, x)
                row_suffixes[-1].append(curr_max)
            row_suffixes[-1] = row_suffixes[-1][::-1]

        col_prefixes = []
        col_suffixes = []
        for c in range(len(height_map[0])):
            col_prefixes.append([])
            curr_max = 0
            for row in height_map:
                x = row[c]
                curr_max = max(curr_max, x)
                col_prefixes[-1].append(curr_max)

            col_suffixes.append([])
            curr_max = 0
            for row in reversed(height_map):
                x = row[c]
                curr_max = max(curr_max, x)
                col_suffixes[-1].append(curr_max)
            col_suffixes[-1] = col_suffixes[-1][::-1]

        def get_min(r, c):
            min_west = min_east = min_north = min_south = 0
            if c - 1 >= 0:
                min_west = row_prefixes[r][c-1]
            if c + 1 < len(height_map[r]):
                min_east = row_suffixes[r][c+1]
            if r - 1 >= 0:
                min_north = col_prefixes[c][r-1]
            if r + 1 < len(height_map):
                min_south = col_prefixes[c][r+1]
            return min(min_west, min_east, min_north, min_south)

        soln = 0
        for r, row in enumerate(height_map):
            for c, height in enumerate(row):
                min_wall = get_min(r, c)
                if height < min_wall:
                    soln += min_wall - height
        return soln



def test_1():
    height_map = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    expected = 4
    assert Solution().trapRainWater(height_map) == expected


def test_2():
    height_map = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    expected = 10
    assert Solution().trapRainWater(height_map) == expected


def test_3():
    "WA"
    height_map = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]] 
    expected = 14
    assert Solution().trapRainWater(height_map) == expected

