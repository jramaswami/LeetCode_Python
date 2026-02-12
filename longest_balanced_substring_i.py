"""
LeetCode
3713. Longest Balanced Substring I
February 2026 Challenge
jramaswami
"""


import string
import itertools


class Solution:
    def longestBalanced(self, word: str) -> int:
        prefixes = [
            list(itertools.accumulate(
                1 if letter == char else 0
                for letter in word
            ))
            for char in string.ascii_lowercase
        ]

        def get(letter_index, left, right):
            if left == 0:
                return prefixes[letter_index][right]
            a = prefixes[letter_index][left - 1]
            b = prefixes[letter_index][right]
            return b - a

        # left, right are inclusive
        for length in range(len(word), 0, -1):
            for left in range(len(word)):
                right = left + length - 1
                if right >= len(word):
                    break

                freqs = []
                for i in range(26):
                    x = get(i, left, right)
                    if x:
                        freqs.append(x)
                if freqs and all(x == freqs[0] for x in freqs):
                    return length
        return 0