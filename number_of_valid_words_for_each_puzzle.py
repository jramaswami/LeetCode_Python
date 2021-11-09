"""
LeetCode :: November 2021 Challenge :: 1178. Number of Valid Words for Each Puzzle
jramaswami

Thank You Larry!
"""


import collections


class Solution:
    def findNumOfValidWords(self, words, puzzles):

        ORD_a = ord('a')

        def letter_to_bit(c):
            """Convert single letter into a bitmask."""
            return 1 << (ord(c) - ORD_a)

        def word_to_bitmask(word):
            """Convert the characters in word into a bitmask."""
            word_mask = 0
            for c in word:
                word_mask |= letter_to_bit(c)
            return word_mask

        def popcount(x):
            """Return the number of bits set in x."""
            bits = 0
            while x:
                if x & 1:
                    bits += 1
                x = x >> 1
            return bits

        # Turn words into bitmasks.  Since puzzles have seven letters,
        # only keep track of bitmasks with less than 7 ones.
        # In addition, any words that have the same mask can be combined.
        word_masks = collections.defaultdict(int)
        for word in words:
            mask = word_to_bitmask(word)
            if popcount(mask) <= 7:
                word_masks[mask] += 1

        # Each puzzle is only 7 characters long.  The first character is fixed
        # giving us only 6 characters that can change.  The superset of 6
        # items is only 2^6 or 64 possible combinations of letters.  Given the
        # constraints where there are up to 10^5 words and 10^4 puzzles,
        # comparing each word with each puzzle is O(10^9) where using all
        # possible subsets of each puzzle is only O(10^4 * 64) or approximately
        # O(7 * 10^5).
        def puzzle_mask_generator(puzzle, index, prev_mask):
            if index >= len(puzzle):
                yield prev_mask
            else:
                # You can include the character at the given index.
                yield from puzzle_mask_generator(
                    puzzle, index + 1, prev_mask | letter_to_bit(puzzle[index])
                )

                # You can skip the character at the given index.
                yield from puzzle_mask_generator(puzzle, index + 1, prev_mask)

        # Compute solution.
        soln = [0 for _ in puzzles]
        for i, puzzle in enumerate(puzzles):
            for puzzle_mask in puzzle_mask_generator(puzzle, 1, letter_to_bit(puzzle[0])):
                soln[i] += word_masks[puzzle_mask]
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