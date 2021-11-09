"""
LeetCode :: November 2021 Challenge :: 1178. Number of Valid Words for Each Puzzle
jramaswami
"""


class Solution:
    def findNumOfValidWords(self, words, puzzles):
        word_letters = [set(word) for word in words]
        puzzle_letters = [set(puzzle) for puzzle in puzzles]
        soln = [0 for _ in puzzles]
        for i, word in enumerate(word_letters):
            for j, puzzle in enumerate(puzzle_letters):
                if puzzles[j][0] in word and all(c in puzzle for c in word):
                    soln[j] += 1
        return soln



def test_1():
    words = ["aaaa","asas","able","ability","actt","actor","access"]
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    expected = [1,1,3,2,4,0]
    assert Solution().findNumOfValidWords(words, puzzles) == expected


def test_2():
    words = ["apple","pleas","please"]
    puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
    expected = [0,1,3,2,0]
    assert Solution().findNumOfValidWords(words, puzzles) == expected