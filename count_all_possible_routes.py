"""
LeetCode
1575. Count All Possible Routes
June 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = pow(10, 9) + 7
        # dp[fuel remaining][location index] = number of ways to arrive
        dp = [[0 for _ in locations] for _ in range(fuel+1)]
        # Initial way to sit at start with no fuel consumed
        dp[fuel][start] = 1
        for fuel_remaining in range(fuel, 0, -1):
            for i, p1 in enumerate(locations):
                if dp[fuel_remaining][i] == 0:
                    continue
                for j, p2 in enumerate(locations):
                    if i == j:
                        continue
                    fuel_consumed = abs(p1 - p2)
                    if fuel_remaining >= fuel_consumed:
                        dp[fuel_remaining - fuel_consumed][j] += dp[fuel_remaining][i]
                        dp[fuel_remaining - fuel_consumed][j] %= MOD

        soln = 0
        for fuel_remaining in range(fuel, -1, -1):
            soln += dp[fuel_remaining][finish]
            soln %= MOD
        return soln % MOD



def test_1():
    locations = [2,3,6,8,4]
    start = 1
    finish = 3
    fuel = 5
    expected = 4
    assert Solution().countRoutes(locations, start, finish, fuel) == expected
    

def test_2():
    locations = [4,3,1]
    start = 1
    finish = 0
    fuel = 6
    expected = 5
    assert Solution().countRoutes(locations, start, finish, fuel) == expected


def test_3():
    locations = [5,2,1]
    start = 0
    finish = 2
    fuel = 3
    expected = 0
    assert Solution().countRoutes(locations, start, finish, fuel) == expected
