"""
LeetCode
2038. Remove Colored Pieces if Both Neighbors are the Same Color
October 2023 Challenge
jramaswami
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alices_winners = bobs_winners = 0
        for i, _ in enumerate(colors[1:-1], start=1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    alices_winners += 1
                else:
                    bobs_winners += 1
        return alices_winners > bobs_winners


def test_1():
    colors = "AAABABB"
    expected = True
    assert Solution().winnerOfGame(colors) == expected


def test_2():
    colors = "AA"
    expected = False
    assert Solution().winnerOfGame(colors) == expected


def test_3():
    colors = "ABBBBBBBAAA"
    expected = False
    assert Solution().winnerOfGame(colors) == expected