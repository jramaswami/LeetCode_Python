"""
LeetCode
874. Walking Robot Simulation
September 2024 Challenge
jramaswami
"""


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirns = ((0, 1), (1, 0), (0, -1), (-1, 0))  # N E S W
        heading = 0
        obstacles = set((x,y) for x, y in obstacles)
        x = y = 0
        soln = 0
        for cmd in commands:
            if cmd == -1:
                # Turn right 90
                heading = (heading + 1) % len(dirns)
            elif cmd == -2:
                # Turn left 90
                heading = (heading - 1 + len(dirns)) % len(dirns)
            else:
                dx, dy = dirns[heading]
                for _ in range(cmd):
                    x0, y0 = x + dx, y + dy
                    if (x0, y0) not in obstacles:
                        x, y = x0, y0
                soln = max(soln, (x * x)+(y*y))
        return soln
