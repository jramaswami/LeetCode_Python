"""
LeetCode :: November 2021 Challenge :: 1178. Number of Valid Words for Each Puzzle
jramaswami
"""


class Solution:
    def findNumOfValidWords(self, words, puzzles):
        def word_to_bitmask(word):
            word_mask = 0
            for c in word:
                word_mask |= 1 << (ord(c) - ord('a'))
            return word_mask

        def first_letter_valid(puzzle, word_mask):
            puzzle_bit = 1 << (ord(puzzle[0]) - ord('a'))
            return puzzle_bit & word_mask

        word_letters = [word_to_bitmask(word) for word in words]
        puzzle_letters = [word_to_bitmask(puzzle) for puzzle in puzzles]
        soln = [0 for _ in puzzles]
        for i, word in enumerate(word_letters):
            for j, puzzle in enumerate(puzzle_letters):
                if first_letter_valid(puzzles[j], word) and word & puzzle == word:
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