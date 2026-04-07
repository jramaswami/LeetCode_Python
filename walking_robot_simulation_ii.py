"""
LeetCode
2069. Walking Robot Simulation II
April 2026 Challenge
jramaswami
"""


EAST, NORTH, WEST, SOUTH = 0, 1, 2, 3


class Robot:

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.dirn = 0
        self.directions = ('East', 'North', 'West', 'South')
        self.x = self.y = 0

    def step(self, num: int) -> None:
        # Base case
        if num == 0:
            return

        steps = 0
        next_x, next_y = self.x, self.y
        if self.dirn == EAST:
            next_x = min(self.x + num, self.width - 1)
            steps = next_x - self.x
        elif self.dirn == WEST:
            next_x = max(self.x - num, 0)
            steps = self.x - next_x
        elif self.dirn == NORTH:
            next_y = min(self.y + num, self.height - 1)
            steps = next_y - self.y
        elif self.dirn == WEST:
            next_y = max(self.y - num, 0)
            steps = self.y - next_y

        if steps == 0:
                self.dirn = (self.dirn + 1) % len(directions)
        self.x, self.y = next_x, next_y
        self.step(self, num - steps)

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.directions[self.dirn]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()