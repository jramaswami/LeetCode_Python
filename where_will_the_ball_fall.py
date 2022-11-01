"""
LeetCode :: 1706. Where Will the Ball Fall
November 2022 Challenge
jramaswami
"""


from typing import *
import collections


Posn = collections.namedtuple('Posn', ['row', 'col'])
Dirn = collections.namedtuple('Dirn', ['dr', 'dc'])
Ball = collections.namedtuple('Ball', ['posn', 'dirn'])


DOWN = Dirn(1, 0)
LEFT = Dirn(0, -1)
RIGHT = Dirn(0, 1)
STUCK = Dirn(-1, -1)
GOAL = Dirn(0, 0)


TRANSITIONS = {
    DOWN: {1: RIGHT, -1: LEFT},
    RIGHT: {1: DOWN, -1: STUCK},
    LEFT: {1: STUCK, -1: DOWN}
}


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        M = len(grid[0])

        def inbounds(posn):
            "Return True if posn is inbounds on grid."
            return (
                posn.row >= 0 and posn.row < N and
                posn.col >= 0 and posn.col < M
            )

        def goal(posn):
            "Return True if the ball has fallen out of the bottom."
            return posn.row == N

        def move(ball):
            "Return a new ball with the appropriate posn and dirn."
            posn0 = Posn(ball.posn.row + ball.dirn.dr, ball.posn.col + ball.dirn.dc)
            dirn0 = STUCK
            if goal(posn0):
                dirn0 = GOAL
            elif inbounds(posn0):
                x = grid[posn0.row][posn0.col]
                dirn0 = TRANSITIONS[ball.dirn][x]
            return Ball(posn0, dirn0)

        # Simulate each ball in turn.
        soln = [-1 for _ in grid[0]]
        for i, _ in enumerate(grid[0]):
            ball = Ball(Posn(-1, i), DOWN)
            while ball.dirn not in [STUCK, GOAL]:
                ball = move(ball)
            if ball.dirn == GOAL:
                soln[i] = ball.posn.col
        return soln


def test_1():
    grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    expected = [1,-1,-1,-1,-1]
    assert Solution().findBall(grid) == expected


def test_2():
    grid = [[-1]]
    expected = [-1]
    assert Solution().findBall(grid) == expected


def test_3():
    grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    expected = [0,1,2,3,4,-1]
    assert Solution().findBall(grid) == expected