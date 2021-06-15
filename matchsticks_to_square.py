"""
LeetCode :: June 2021 Challenge :: Matchsticks to Square
jramaswami
"""


from typing import *
import sys


sys.setrecursionlimit(pow(10, 9))


def partition_sides(matchsticks, target):
    """
    Find all possible sides that add up to the target sum.

    Since there are only up to 15 matches, we can do this using a bitmask.
    There is at most 2^15 possible combinations.
    """
    T = []
    LIMIT = 2 ** len(matchsticks)
    for mask in range(LIMIT):
        matchstick_sum = 0
        for bit, matchstick in enumerate(matchsticks):
            if mask & (1 << bit):
                matchstick_sum += matchstick
        if matchstick_sum == target:
            T.append(mask)
    return T


def find_four(p, length, acc, possible_sides):
    """
    Recursively search for four sides that do not overlap.
    """
    if length == 4:
        return True

    if p >= len(possible_sides):
        return False

    # I can include possible_sides[p] only if it does not overlap with
    # previous sides.
    if acc ^ possible_sides[p] == acc + possible_sides[p]:
        soln = find_four(p + 1, length + 1, acc + possible_sides[p], possible_sides)
        soln = soln or find_four(p + 1, length, acc, possible_sides)
    else:
        soln = find_four(p + 1, length, acc, possible_sides)
    return soln


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # A square is made of of 4 equal sides.  The sum of the 
        # matchsticks must be divisible by 4.
        sides_sum = sum(matchsticks)
        if sides_sum % 4:
            return False

        # Generate all the sides
        side_length = sides_sum // 4
        possible_sides = partition_sides(matchsticks, side_length)

        # See if have four unique sides.
        return find_four(0, 0, 0, possible_sides)
        


def test_1():
    matchsticks = [1,1,2,2,2]
    assert Solution().makesquare(matchsticks) == True


def test_2():
    matchsticks = [3,3,3,3,4]
    assert Solution().makesquare(matchsticks) == False


def test_3():
    matchsticks = [1] * 16
    assert Solution().makesquare(matchsticks) == True

