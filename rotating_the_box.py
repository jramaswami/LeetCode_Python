"""
LeetCode
1861. Rotating the Box
November 2024 Challenge
jramaswami
"""


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        N = len(box)
        M = len(box[0])
        # Rotate the box
        box0 = [[0 for _ in range(N)] for _ in range(M)]
        for r, row in enumerate(box):
            for c, x in enumerate(row):
                r0 = c
                c0 = N - 1 - r
                box0[r0][c0] = x
        # Move rocks from bottom up.
        for c in range(N):
            empty_space = M-1
            for r in range(M-1,-1,-1):
                if box0[r][c] == '.':
                    pass
                elif box0[r][c] == '*':
                    # If there is a stationary object then
                    # the next empty space must be above it.
                    empty_space = r-1
                elif box0[r][c] == '#':
                    if empty_space > r:
                        # If there is an empty space, move the rock
                        # into it. Then the next empty space must be
                        # above the rock.
                        box0[empty_space][c] = '#'
                        box0[r][c] = '.'
                        empty_space = empty_space - 1
                    else:
                        # If there is a rock then
                        # the next empty space must be above it.
                        empty_space = r - 1
        return box0
