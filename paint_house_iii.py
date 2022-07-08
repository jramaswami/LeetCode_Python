"""
LeetCode :: July 2022 Challenge :: 1473. Paint House III
jramaswami
"""


import math
import functools


class Solution:

    def minCost(self, houses, cost, house_count, color_count, target):

        @functools.cache
        def solve0(prev_house, prev_color, prev_neighborhoods):
            # Base Case: too many neighborhoods.
            if prev_neighborhoods > target:
                return math.inf

            curr_house = prev_house + 1

            # Base Case: all houses painted.
            if curr_house > house_count:
                # Did we reach the required number of neighborhoods?
                if prev_neighborhoods < target:
                    return math.inf
                return 0

            # Should this house be painted?
            if houses[curr_house - 1] == 0:
                # This house should be painted.
                result = math.inf
                for paint_color in range(1, color_count+1):
                    paint_cost = cost[curr_house-1][paint_color-1]
                    curr_neighborhoods = (prev_neighborhoods if paint_color == prev_color else prev_neighborhoods + 1)
                    result = min(
                        result,
                        paint_cost + solve0(curr_house, paint_color, curr_neighborhoods)
                    )
                return result
            else:
                # This house should not be painted.
                paint_color = houses[curr_house - 1]
                if paint_color == prev_color:
                    return solve0(curr_house, paint_color, prev_neighborhoods)
                else:
                    return solve0(curr_house, paint_color, prev_neighborhoods + 1)

        soln = solve0(0, 0, 0)
        return -1 if soln == math.inf else soln



def test_1():
    houses = [0,0,0,0,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3
    expected = 9
    assert Solution().minCost(houses, cost, m, n, target) == expected


def test_2():
    houses = [0,2,1,2,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3
    expected = 11
    assert Solution().minCost(houses, cost, m, n, target) == expected


def test_3():
    houses = [3,1,2,3]
    cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
    m = 4
    n = 3
    target = 3
    expected = -1
    assert Solution().minCost(houses, cost, m, n, target) == expected


def test_4():
    "WA"
    houses = [0,0,0,1]
    cost = [[1,5],[4,1],[1,3],[4,4]]
    m = 4
    n = 2
    target = 4
    expected = 12
    assert Solution().minCost(houses, cost, m, n, target) == expected
