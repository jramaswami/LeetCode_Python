"""
Leetcode :: August 2021 Challenge :: Stone Game
https://leetcode.com/problems/stone-game/

Dyanamic Programming Solution
------------------------------------------------------------------------
REF: https://www.youtube.com/watch?v=WxpIHvsu1RI

For player that goes first
(1) Pick left -> T[i+1][j].second + A[i]
(2) Pick right -> T[i][j-1].second + A[j])
Choose the maximum of the two and put it in T[i][j].first

For the player that goes second
(1) 1st player chose left -> T[i][j].second = T[i+1][j].first
(2) 1st player chose right -> T[i][j].second = T[i][j-1].first

Mathematical Solution
-----------------------------------------------------------------------
REF: https://www.tutorialcup.com/leetcode-solutions/stone-game.htm

Observe that the number of piles is even.  If the first player takes the
0 indexed, or first even indexed, pile then the second player can only
choose an odd indexed pile. If the first player chooses the last or N-1th
indexed stone, which is odd indexed, then the second player can only choose
an even indexed stone.

This means that the first player can choose to take all the even indexed piles
or all the odd indexed piles.

Also, observe that the number of stones is odd, so there are not ties, that is,
no way for the two sums to ever be the same.  So, the first player can choose
to take even or odd stones, whichever sums to the most.  Since one or the other
must be greater, the first player *always wins*!

"""

class Solution:
    def stoneGame(self, piles):
        dp = [[None for _ in piles] for _ in piles]

        # Init diagonal
        for i, _ in enumerate(piles):
            dp[i][i] = (piles[i], 0)

        for c,_ in enumerate(dp[1:], start=1):
            i = 0
            j = c
            while i < len(dp) and j < len(dp[0]):
                # print(i, j)
                left = dp[i+1][j][1] + piles[i]
                right = dp[i][j-1][1] + piles[j]
                if left > right:
                    dp[i][j] = (left, dp[i+1][j][0])
                else:
                    dp[i][j] = (right, dp[i][j-1][0])

                i += 1
                j += 1

        return dp[0][-1][0] > dp[0][-1][1]



def test_sample_test():
    solver = Solution()
    assert solver.stoneGame([5,3,4,5]) == True


def test_failed_test():
    solver = Solution()
    assert solver.stoneGame([3, 7, 2, 3]) == True


def test_random():
    import random
    for _ in range(20):
        N = 500
        A = [random.randint(1, 500) for _ in range(N)]
        S = sum(A)
        if S % 2 == 0:
            A[-1] -= 1
        assert Solution().stoneGame(A) == True
