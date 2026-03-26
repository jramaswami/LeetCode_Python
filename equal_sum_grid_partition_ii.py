"""
LeetCode
3548. Equal Sum Grid Partition II
March 2026 Challenge
jramaswami
"""


import itertools
import collections
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        def can_cut(g):
            if len(g) == 1:
                return False
            R, C = len(g), len(g[0])
            top_sum = 0
            bottom_sum = sum(itertools.chain.from_iterable(row for row in g))
            top_elements = collections.Counter()
            bottom_elements = collections.Counter(
                itertools.chain.from_iterable(row for row in g)
            )
            for r, row in enumerate(grid[:-1]):
                # Remove elements from bottom and place in top
                # Remove from bottom sum and add to top sum
                for x in row:
                    top_elements[x] += 1
                    bottom_elements[x] -= 1
                    top_sum += x
                    bottom_sum -= x
                # See if we can satisfy top_sum == bottom_sum
                if top_sum == bottom_sum:
                    return True
                elif top_sum > bottom_sum:
                    # Must remove from top to satisfy
                    delta = top_sum - bottom_sum
                    if r == 0:
                        # On top we can only remove ends
                        if delta in (g[0][0], g[0][-1]):
                            return True
                    elif top_elements[delta] >= 1:
                        return True
                else:
                    # Must remove from bottom row
                    delta = bottom_sum - top_sum
                    if r == len(grid) - 2:
                        # On bottom we can only remove ends
                        if len(g[0]) > 1 and delta in (g[-1][0], g[-1][-1]):
                            return True
                    elif bottom_elements[delta] >= 1:
                        return True
            return False

        def rotate(g):
            h = []
            for c, _ in enumerate(g[0]):
                h.append([])
                for r, _ in enumerate(g):
                    h[-1].append(g[r][c])
            return h

        return can_cut(grid) or can_cut(rotate(grid))


def test_1():
    grid = [[1,4],[2,3]]
    expected = True
    assert Solution().canPartitionGrid(grid) == expected


def test_2():
    grid = [[1,2],[3,4]]
    expected = True
    assert Solution().canPartitionGrid(grid) == expected


def test_3():
    grid = [[1,2,4],[2,3,5]]
    expected = False
    assert Solution().canPartitionGrid(grid) == expected


def test_5():
    "WA"
    grid = [[5,5,6,2,2,2]]
    expected = True
    assert Solution().canPartitionGrid(grid) == expected