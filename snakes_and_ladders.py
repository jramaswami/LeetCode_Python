"""
LeetCode
909. Snakes and Ladders
January 2023 Challenge
jramaswami
"""


from typing import *
import collections


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Convert into dictionary of snakes and ladders.
        snakes_and_ladders = dict()
        i = 1
        for r, row in enumerate(reversed(board)):
            if r % 2:
                # Go backwards
                for cell in reversed(row):
                    if cell >= 0:
                        snakes_and_ladders[i] = cell
                    i += 1
            else:
                # Go forwards
                for cell in row:
                    if cell >= 0:
                        snakes_and_ladders[i] = cell
                    i += 1
        # BFS
        last_cell = i-1
        queue = set()
        new_queue = set()
        queue.add(1)
        if 1 in snakes_and_ladders:
            queue.add(snakes_and_ladders[1])
        dist = 0
        visited = set()
        visited.update(queue)
        while queue:
            for i in queue:
                if i == last_cell:
                    return dist
                for x in range(i+1, min(i+6, last_cell)+1):
                    if x in snakes_and_ladders:
                        if snakes_and_ladders[x] not in visited:
                            new_queue.add(snakes_and_ladders[x])
                            visited.add(snakes_and_ladders[x])
                    elif x not in visited:
                        new_queue.add(x)
                        visited.add(x)
            queue, new_queue = new_queue, set()
            dist += 1
        return -1


def test_1():
    board = [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
    ]
    expected = 4
    assert Solution().snakesAndLadders(board) == expected


def test_2():
    board = [[-1,-1],[-1,3]]
    expected = 1
    assert Solution().snakesAndLadders(board) == expected


def test_3():
    board = [[1,1,-1],[1,1,1],[-1,1,1]]
    expected = -1
    assert Solution().snakesAndLadders(board) == expected


def test_4():
    board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
    expected = 2
    assert Solution().snakesAndLadders(board) == expected
