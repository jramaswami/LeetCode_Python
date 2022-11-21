"""
LeetCode :: 1926. Nearest Exit from Entrance in Maze
November 2022 Challenge
jramaswami
"""


from typing import *
import collections
import math


class Solution:

    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def is_border(r, c):
            "Return True if (r, c) is at the border of maze."
            return r == 0 or r == len(maze) - 1 or c == 0 or c == len(maze[r]) - 1

        def is_exit(r, c):
            "Return True if (r, c) is an exit."
            return is_border(r, c) and not (r == entrance[0] and c == entrance[1])

        def inbounds(r, c):
            "Return True if (r, c) is inside maze boundaries."
            return r >= 0 and r < len(maze) and c >= 0 and c < len(maze[r])

        def neighbors(r, c):
            "Generator returning found neighbors."
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def is_hall(r, c):
            "Return True if (r, c) is a hall."
            return maze[r][c] == '.'

        dist = [[math.inf for _ in row] for row in maze]
        queue = collections.deque()
        queue.append((entrance[0], entrance[1]))
        dist[entrance[0]][entrance[1]] = 0
        soln = math.inf
        while queue:
            r, c = queue.popleft()
            if is_exit(r, c):
                return dist[r][c]
            for r0, c0 in neighbors(r, c):
                if is_hall(r0, c0) and dist[r][c] + 1 < dist[r0][c0]:
                    dist[r0][c0] = dist[r][c] + 1
                    queue.append((r0, c0))

        return -1



def test_1():
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    expected = 1
    assert Solution().nearestExit(maze, entrance) == expected


def test_2():
    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance = [1,0]
    expected = 2
    assert Solution().nearestExit(maze, entrance) == expected


def test_3():
    maze = [[".","+"]]
    entrance = [0,0]
    expected = -1
    assert Solution().nearestExit(maze, entrance) == expected
