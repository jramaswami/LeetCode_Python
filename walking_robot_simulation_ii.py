"""
LeetCode
2069. Walking Robot Simulation II
April 2026 Challenge
jramaswami
"""


class Robot:

    def __init__(self, width: int, height: int):
        self.cells = []
        for x in range(width):
            self.cells.append((x, 0))
        for y in range(1, height):
            self.cells.append((width-1, y))
        for x in range(width-2,-1,-1):
            self.cells.append((x, height-1))
        for y in range(height-2, 0, -1):
            self.cells.append((0, y))
        self.steps = 0
        self.width, self.height = width, height

    def step(self, num: int) -> None:
        self.steps += num

    def getPos(self) -> List[int]:
        return self.cells[self.steps % len(self.cells)]

    def getDir(self) -> str:
        x, y = self.getPos()
        if self.steps == 0:
            return 'East'
        if x > 0 and y == 0:
            return 'East'
        if x == self.width - 1:
            return 'North'
        if y == self.height - 1:
            return 'West'
        if x == 0:
            return 'South'