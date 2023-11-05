"""
LeetCode
1535. Find the Winner of an Array Game
November 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        wins = 0
        for n in arr[1:]:
            if winner < n:
                winner = n
                wins = 1
            else:
                wins += 1
            if wins >= k:
                return winner
        return winner