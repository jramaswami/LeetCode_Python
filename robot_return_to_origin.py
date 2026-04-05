"""
LeetCode
657. Robot Return to Origin
April 2026 Challenge
jramaswami
"""


import dataclasses


@dataclasses.dataclass(frozen = True)
class Posn:
    x: int
    y: int

    def __add__(self, other):
        return Posn(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        M = {'R': Posn(1, 0), 'L': Posn(-1, 0), 'U': Posn(0, 1), 'D': Posn(0, -1)}
        origin = Posn(0, 0)
        curr = Posn(0, 0)
        for move in moves:
            curr = curr + M[move]
        return curr == origin