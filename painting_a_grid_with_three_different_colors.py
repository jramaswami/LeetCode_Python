"""
LeetCode
1931. Painting a Grid With Three Different Colors
May 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # Get all the possible column configurations
        possible_columns = []
        def rec(i, acc):
            if i >= m:
                possible_columns.append(tuple(acc))
            else:
                for c in range(3):
                    if (not acc) or acc[-1] != c:
                        acc.append(c)
                        rec(i+1, acc)
                        acc.pop()

        rec(0, [])

        # Build a graph of nonoverlapping column configurations
        def overlap(left, right):
            return any(a == b for a, b in zip(left, right))

        graph = [[] for _ in possible_columns]
        for i, left in enumerate(possible_columns):
            for j, right in enumerate(possible_columns[i+1:], start=i+1):
                if not overlap(left, right):
                    graph[i].append(j)
                    graph[j].append(i)

        MOD = pow(10,9)+7
        # dp[column config][column index] = number of ways
        dp = [[0 for _ in range(n)] for _ in possible_columns]
        # Initialize one way for each column config in the first column
        for i, _ in enumerate(possible_columns):
            dp[i][0] = 1

        for j in range(n-1):
            # Going from column j to column j+1
            for i, _ in enumerate(possible_columns):
                # For each column configuration
                for k in graph[i]:
                    # Add my total to any valid next column configuration
                    dp[k][j+1] += dp[i][j]
                    dp[k][j+1] %= MOD

        soln = 0
        for row in dp:
            soln += row[-1]
            soln %= MOD
        return soln


def test_3():
    m = n = 5
    assert Solution().colorTheGrid(m,n) == 580986