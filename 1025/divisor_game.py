"""
Leetcode :: 1025. Divisor Game
https://leetcode.com/problems/divisor-game/
"""

class Solution:
    def divisorGame(self, N):
        dp = [0 for _ in range(N+1)]
        for state in range(N+1):
            for i in range(1, state):
                if state % i == 0 and dp[state - i] == 0:
                    dp[state] = 1
        print(dp)
        return dp[N] == 1


def test_1():
    solver = Solution()
    assert solver.divisorGame(2) == True
    

def test_2():
    solver = Solution()
    assert solver.divisorGame(3) == False
