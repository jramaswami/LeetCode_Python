"""
LeetCode
1411. Number of Ways to Paint N x 3 Grid
January 2026 Challenge
jramaswami
"""


class Solution:
    def numOfWays(self, n: int) -> int:
        # All possible rows of tiles
        PS = (
            'ryr', 'ryg', 'rgr', 'rgy',
            'yry', 'yrg', 'ygr', 'ygy',
            'gry', 'grg', 'gyr', 'gyg',
        )

        if n == 1:
            return len(PS)

        # Graph of transitions
        graph = [[] for _ in PS]
        for i, a in enumerate(PS):
            for j, b in enumerate(PS):
                if all(x != y for x, y in zip(a, b)):
                    graph[i].append(j)

        MOD = pow(10, 9) + 7

        # dp[p][i] = count
        dp = [[0 for _ in range(n)] for _ in PS]

        # Initialize 1 for each possible starting row
        for j, _ in enumerate(PS):
            dp[j][0] = 1

        # Compute
        for i in range(n-1):
            for j, row in enumerate(PS):
                for k in graph[j]:
                    dp[k][i+1] += dp[j][i]
                    dp[k][i+1] %= MOD

        # Sum solution
        soln = 0
        for j, _ in enumerate(PS):
            soln += dp[j][n-1]
            soln %= MOD
        return soln