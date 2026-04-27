"""
LeetCode
1391. Check if There is a Valid Path in a Grid
April 2026 Challenge
jramaswami
"""


import collections
import dataclasses


@dataclasses.dataclass(frozen=True)
class Posn:
    row: int
    col: int

    def __add__(self, other):
        return Posn(self.row + other.row, self.col + other.col)

    def inv(self):
        return Posn(-self.row, -self.col)


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def inbounds(p):
            return 0 <= p.row < len(grid) and 0 <= p.col < len(grid[p.row])

        roads = [
            [],
            [Posn(0, 1), Posn(0, -1)],
            [Posn(1, 0), Posn(-1, 0)],
            [Posn(1, 0), Posn(0, -1)],
            [Posn(1, 0), Posn(0, 1)],
            [Posn(-1, 0), Posn(0, -1)],
            [Posn(-1, 0), Posn(0, 1)]
        ]

        graph = collections.defaultdict(set)
        for r, row in enumerate(grid):
            for c, road_index in enumerate(row):
                curr = Posn(r, c)
                for curr_road in roads[road_index]:
                    neighbor = curr + curr_road
                    if inbounds(neighbor):
                        neighbor_index = grid[neighbor.row][neighbor.col]
                        if curr_road.inv() in roads[neighbor_index]:
                            graph[curr].add(neighbor)

        origin = Posn(0, 0)
        dest = Posn(len(grid)-1, len(grid[0])-1)
        queue = collections.deque()
        queue.append(origin)
        visited = set()
        visited.add(set)
        while queue:
            curr = queue.popleft()
            if curr == dest:
                return True
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False