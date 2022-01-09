"""
LeetCode :: January 2022 Challenge :: 1041. Robot Bounded In Circle
jramaswami
"""


# X, Y
#                N       E       S        W
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:

    def isRobotBounded(self, instructions):


        def move(dirn, posn):
            return (
                posn[0] + (1 * DIRECTIONS[dirn][0]),
                posn[1] + (1 * DIRECTIONS[dirn][1])
            )

        def turn(dirn, t):
            if t < 0:
                # Left
                dirn -= 1
                if dirn < 0:
                    dirn = 3
            else:
                dirn += 1
                if dirn > 3:
                    dirn = 0
            return dirn

        def perform(posn, dirn, instructions):
            for instr in instructions:
                if instr == 'G':
                    posn = move(dirn, posn)
                elif instr == 'L':
                    dirn = turn(dirn, -1)
                else:
                    dirn = turn(dirn, 1)
            return posn, dirn

        dirn = 0
        posn = (0, 0)
        for _ in range(4):
            posn, dirn = perform(posn, dirn, instructions)
            if posn == (0, 0):
                return True
        return False


def test_1():
    instructions = "GGLLGG"
    assert Solution().isRobotBounded(instructions) == True


def test_2():
    instructions = "GG"
    assert Solution().isRobotBounded(instructions) == False


def test_3():
    instructions = "GL"
    assert Solution().isRobotBounded(instructions) == True
