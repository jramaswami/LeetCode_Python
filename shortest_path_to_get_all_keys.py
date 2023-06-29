"""
LeetCode
864. Shortest Path to Get All Keys
June 2023 Challenge
jramaswami
"""


import functools
import collections
from typing import List


Posn = collections.namedtuple('Posn', ['row', 'col'])
QItem = collections.namedtuple('QItem', ['dist', 'posn'])


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        INF = pow(10,20)
        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def is_key(grid_val):
            return grid_val in 'abcdef'

        def is_door(grid_val):
            return grid_val in 'ABCDEF'

        def is_wall(posn):
            return grid[posn.row][posn.col] == '#'

        def key_index(key):
            return ord(key) - ord('a')

        def have_key(key, keys_acc):
            i = key_index(key)
            return ((1 << i) & keys_acc) > 0

        def add_key(key, keys_acc):
            i = key_index(key)
            return ((1 << i) | keys_acc)

        def inbounds(posn):
            return (
                posn.row >= 0 and posn.col >= 0 and
                posn.row < len(grid) and posn.col < len(grid[posn.row])
            )

        def neighbors(posn):
            for dr, dc in OFFSETS:
                posn0 = Posn(posn.row + dr, posn.col + dc)
                if inbounds(posn0):
                    yield posn0

        @functools.cache
        def bfs(start, target, keys_acc):
            queue = collections.deque([QItem(0, start)])
            visited = [[False for _ in row] for row in grid]
            visited[start.row][start.col] = True
            while queue:
                item = queue.popleft()
                if item.posn == target:
                    return item.dist
                for neighbor in neighbors(item.posn):
                    if visited[neighbor.row][neighbor.col]:
                        continue
                    if is_wall(neighbor):
                        continue
                    neighbor_val = grid[neighbor.row][neighbor.col]
                    if is_door(neighbor_val):
                        door_key = neighbor_val.lower()
                        if have_key(door_key, keys_acc):
                            visited[neighbor.row][neighbor.col] = True
                            queue.append(QItem(item.dist+1, neighbor))
                    else:
                        visited[neighbor.row][neighbor.col] = True
                        queue.append(QItem(item.dist+1, neighbor))
            return INF

        # Get locations of all keys
        locations = dict()
        keys_to_find = []
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if is_key(val):
                    keys_to_find.append(val)
                    locations[val] = Posn(r, c)
                elif val == '@':
                    locations[val] = Posn(r, c)

        ALL_KEYS = (1 << len(keys_to_find)) - 1

        @functools.cache
        def rec(curr, keys_acc):
            if keys_acc == ALL_KEYS:
                return 0

            result = INF
            for key in keys_to_find:
                if not have_key(key, keys_acc):
                    dist = bfs(locations[curr], locations[key], keys_acc)
                    if dist < INF:
                        result = min(
                            dist + rec(key, add_key(key, keys_acc)),
                            result
                        )
            return result

        soln = rec('@', 0)
        return -1 if soln == INF else soln


def test_1():
    grid = ["@.a..","###.#","b.A.B"]
    expected = 8
    assert Solution().shortestPathAllKeys(grid) == expected


def test_2():
    grid = ["@..aA","..B#.","....b"]
    expected = 6
    assert Solution().shortestPathAllKeys(grid) == expected


def test_3():
    grid = ["@Aa"]
    expected = -1
    assert Solution().shortestPathAllKeys(grid) == expected
