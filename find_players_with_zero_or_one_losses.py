"""
LeetCode :: 2225. Find Players With Zero or One Losses
November 2022 Challenge
jramaswami
"""


from typing import *


class Player:

    def __init__(self, id):
        self.id = id
        self.wins = 0
        self.losses = 0

    def win(self):
        self.wins += 1

    def lose(self):
        self.losses += 1

    def __repr__(self):
        return f"Player(id={self.id}, wins={self.wins}, losses={self.losses})"


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = dict()
        for winner, loser in matches:
            if winner not in players:
                players[winner] = Player(winner)
            if loser not in players:
                players[loser] = Player(loser)
            players[winner].win()
            players[loser].lose()

        soln = [[], []]
        for p in sorted(players):
            if players[p].losses == 0:
                soln[0].append(p)
            elif players[p].losses == 1:
                soln[1].append(p)
        return soln


def test_1():
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    expected = [[1,2,10],[4,5,7,8]]
    result = Solution().findWinners(matches)
    result[0].sort()
    result[1].sort()
    expected[0].sort()
    expected[1].sort()
    assert result == expected


def test_2():
    matches = [[2,3],[1,3],[5,4],[6,4]]
    expected = [[1,2,5,6],[]]
    result = Solution().findWinners(matches)
    result[0].sort()
    result[1].sort()
    expected[0].sort()
    expected[1].sort()
    assert result == expected