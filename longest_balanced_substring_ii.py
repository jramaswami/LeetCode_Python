"""
LeetCode
3713. Longest Balanced Substring II
February 2026 Challenge
jramaswami

REF: https://dev.to/om_shree_0709/beginner-friendly-guide-longest-balanced-substring-ii-problem-3714-c-python-javascript-591f
"""


import itertools


class Solution:
    def longestBalanced(self, word: str) -> int:
        soln = 0
        # Longest single
        curr_length = 0
        prev_char = ''
        for curr_char in word:
            if curr_char == prev_char:
                curr_length += 1
            else:
                soln = max(soln, curr_length)
                prev_char = curr_char
                curr_length = 1
        soln = max(soln, curr_length)
        # Longest double
        for char1, char2 in itertools.combinations('abc', 2):
            diff = 0
            first_occ = {0: -1}
            for i, char in enumerate(word):
                if char == char1:
                    diff += 1
                elif char == char2:
                    diff -= 1
                else:
                    first_occ = {0: i}
                    diff = 0
                    continue

                if diff in first_occ:
                    soln = max(soln, i - first_occ[diff])
                else:
                    first_occ[diff] = i
        # Longest triple
        threes = {(0, 0): -1}
        a, b, c = 0, 0, 0
        for i, char in enumerate(word):
            if char == 'a': a += 1
            if char == 'b': b += 1
            if char == 'c': c += 1
            key = (a - b, a - c)
            if key in threes:
                soln = max(soln, i - threes[key])
            else:
                threes[key] = i
        return soln