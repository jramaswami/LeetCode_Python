"""
LeetCode
3197. Find the Minimum Area to Cover All Ones II
August 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/3197
"""


import math
from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def min_area_in_submat(row0, col0, row1, col1):
            min_row = min_col = math.inf
            max_row = max_col = -math.inf
            for r in range(row0, row1+1):
                for c in range(col0, col1+1):
                    if grid[r][c]:
                        min_row = min(min_row, r)
                        min_col = min(min_col, c)
                        max_row = max(max_row, r)
                        max_col = max(max_col, c)
            return (max_row - min_row + 1) * (max_col - min_col + 1)

        row_count, col_count = len(grid), len(grid[0])
        soln = row_count * col_count
        top = left = 0
        bottom, right = row_count - 1, col_count - 1

        # Horizontal splits
        # AA
        # BB
        # CC
        for row_split1 in range(bottom):
            for row_split2 in range(row_split1+1, bottom):
                soln = min(soln,
                    min_area_in_submat(top, left, row_split1, right)+
                    min_area_in_submat(row_split1+1, left, row_split2, right)+
                    min_area_in_submat(row_split2+1, left, bottom, right)
                )

        # Vertical splits
        # ABC
        # ABC
        for col_split1 in range(right):
            for col_split2 in range(col_split1+1, right):
                soln = min(soln,
                    min_area_in_submat(top, left, bottom, col_split1)+
                    min_area_in_submat(top, col_split1+1, bottom, col_split2)+
                    min_area_in_submat(top, col_split2+1, bottom, right)
                )

        # Mixed splits
        for row_split in range(bottom):
            for col_split in range(right):
                #AB
                #AC
                soln = min(soln,
                    min_area_in_submat(top, left, bottom, col_split)+ # A
                    min_area_in_submat(top, col_split+1, row_split, right)+ # B
                    min_area_in_submat(row_split+1, col_split+1, bottom, right) # C
                )
                #AA
                #BC
                soln = min(soln,
                    min_area_in_submat(top, left, row_split, right)+ # A
                    min_area_in_submat(row_split+1, left, bottom, col_split)+ # B
                    min_area_in_submat(row_split+1, col_split+1, bottom, right) # C
                )
                #BA
                #CA
                soln = min(soln,
                    min_area_in_submat(top, left, row_split, col_split)+ # B
                    min_area_in_submat(row_split+1, left, bottom, col_split)+ # C
                    min_area_in_submat(top, col_split+1, bottom, right) # A
                )

                #BC
                #AA
                soln = min(soln,
                    min_area_in_submat(top, left, row_split, col_split)+ # B
                    min_area_in_submat(top, col_split+1, row_split, right)+ # C
                    min_area_in_submat(row_split+1, left, bottom, right) # A
                )
        return soln


def test_1():
    grid = [[1,0,1],[1,1,1]]
    expected = 5
    assert Solution().minimumSum(grid) == expected
