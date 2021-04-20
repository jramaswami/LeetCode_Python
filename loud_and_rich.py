"""
Leetcode :: 851 :: Loud and Rich
https://leetcode.com/contest/weekly-contest-88/problems/loud-and-rich/
"""
from collections import defaultdict
from math import inf


class Solution:
    "Solver"
    def __init__(self):
        self.answer = []
        self.richer = []
        self.quiet = []
        self.tree = defaultdict(list)

    def loudAndRich(self, richer, quiet):
        "Solve"
        self.quiet = quiet
        self.richer = richer

        # Build tree
        for rich, poor in richer:
            self.tree[poor].append(rich)

        # Build answer
        self.answer = [-1 for _ in range(len(self.quiet))]
        for node in range(len(self.quiet)):
            if self.answer[node] == -1:
                self._solve(node)
        return self.answer

    def _solve(self, node):
        "Solve recursively."
        if self.answer[node] > -1:
            return self.answer[node]

        if not self.tree[node]:
            self.answer[node] = node
            return node

        quietest_neighbor = node
        for rich_neighbor in self.tree[node]:
            quiet_neighbor = self._solve(rich_neighbor)
            if self.quiet[quiet_neighbor] < self.quiet[quietest_neighbor]:
                quietest_neighbor = quiet_neighbor
        self.answer[node] = quietest_neighbor
        return quietest_neighbor


def test1():
    "Example 1"
    solver = Solution()
    richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
    quiet = [3,2,5,4,6,1,7,0]
    assert solver.loudAndRich(richer, quiet) == [5,5,2,5,4,5,6,7]