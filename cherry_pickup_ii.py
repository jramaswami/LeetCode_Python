"""
LeetCode :: January 2022 Challenge :: 1463. Cherry Pickup II
jramaswami
"""


import functools


class Solution:
    def cherryPickup(self, grid):

        @functools.cache
        def solve(r, r1c, r2c):
            # Base case: robots have reached the end of the grid.
            if r >= len(grid):
                return 0

            result = 0

            init_result = grid[r][r1c]
            if r1c != r2c:
                init_result += grid[r][r2c]

            for dc1 in (-1, 0, 1):

                r1c0 = r1c + dc1
                # Do not go out of bounds
                if r1c0 >= len(grid[r]) or r1c0 < 0:
                    continue

                for dc2 in (-1, 0, 1):

                    r2c0 = r2c + dc2
                    # Do not go out of bounds
                    if r2c0 >= len(grid[r]) or r2c0 < 0:
                        continue

                    local_result = init_result + solve(r+1, r1c0, r2c0)
                    result = max(result, local_result)

            return result

        return solve(0, 0, len(grid[0]) - 1)



def test_1():
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    assert Solution().cherryPickup(grid) == 24


def test_2():
    grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
    assert Solution().cherryPickup(grid) == 28
