"""
LeetCode :: July 2022 Challenge :: 1473. Paint House III
jramaswami
"""


import math


class Solution:

    def solve(self, houses, cost, house_count, color_count, target):
        # print(f"solve({houses=}, {cost=}, {house_count=}, {color_count=}, {target=})")
        # dp[first i houses][color of i-th house][number of neighborhoods] = min cost
        # [0 to house_count)[0 to color_count]   [0 to house count]
        dp = [[[math.inf for _ in range(target+1)] for _ in range(color_count+1)] for _ in range(house_count+1)]
        for c in range(1, color_count+1):
            # It costs nothing to have no neighborhoods for any color when
            # there are zero houses.
            dp[0][c][0] = 0

        # for t, table in enumerate(dp):
        #     print("painted houses", t)
        #     for row in table:
        #         print(row)
        #     print()

        for i, table in enumerate(dp[1:], start=1):
            for previous_color, row in enumerate(table[1:], start=1):
                for previous_neighborhoods, _ in enumerate(row):
                    if houses[i-1] == 0:
                        for current_color, _ in enumerate(table[1:], start=1):
                            # How much does it cost to do so?
                            painting_cost = cost[i-1][current_color-1]
                            # How many neighborhoods will I have? That depends on what
                            # color the previous house was painted and how many
                            # neighborhoods already existed.
                            current_neighborhoods = previous_neighborhoods
                            if previous_color != current_color:
                                current_neighborhoods += 1
                            # print(f"{i=} {previous_color=} {current_color=} {current_neighborhoods=}")
                            # print(f"{len(dp)=} {len(table)=} {len(row)=}")
                            if current_neighborhoods <= target:
                                previous_cost = dp[i-1][previous_color][previous_neighborhoods]
                                current_cost = previous_cost + painting_cost
                                dp[i][current_color][current_neighborhoods] = min(
                                    dp[i][current_color][current_neighborhoods],
                                    current_cost
                                )
                    else:
                        current_color = houses[i-1]
                        painting_cost = cost[i-1]
                        current_neighborhoods = previous_neighborhoods
                        if previous_color != current_color:
                            current_neighborhoods += 1
                        # print(f"{i=} {previous_color=} {current_color=} {current_neighborhoods=}")
                        # print(f"{len(dp)=} {len(table)=} {len(row)=}")
                        if current_neighborhoods <= target:
                            previous_cost = dp[i-1][previous_color][previous_neighborhoods]
                            current_cost = previous_cost + painting_cost
                            dp[i][current_color][current_neighborhoods] = min(
                                dp[i][current_color][current_neighborhoods],
                                current_cost
                            )


        for t, table in enumerate(dp):
            print("painted houses", t)
            for row in table:
                print(row)
            print()

        return min(dp[-1][color][target] for color in range(1, color_count+1))


def test_1():
    houses = [0,0,0,0,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3
    expected = 9
    assert Solution().solve(houses, cost, m, n, target) == expected
