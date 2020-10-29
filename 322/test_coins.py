"""
Leetcode :: 322. Coin Change
https://leetcode.com/problems/coin-change/
"""
import coins

def test_sample():
    solver = coins.Solution()
    assert solver.coinChange([1, 2, 5], 11) == 3
    assert solver.coinChange([2], 3) == -1
