"""
LeetCode
3121. Count the Number of Special Characters II
May 2026 Challenge
jramaswami
"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = dict()
        first_upper = dict()
        for i, letter in enumerate(word):
            if letter.islower():
                last_lower[letter] = i
            if letter.isupper() and letter not in first_upper:
                first_upper[letter] = i

        soln = 0
        for uppercase_letter in first_upper:
            first_upper_index = first_upper[uppercase_letter]
            lowercase_letter = uppercase_letter.lower()
            if lowercase_letter in last_lower:
                last_lower_index = last_lower[lowercase_letter]
                if first_upper_index > last_lower_index:
                    soln += 1
        return soln