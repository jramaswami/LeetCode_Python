"""
LeetCode
3136. Valid Word
July 2025 Challenge
jramaswami
"""


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = 'AEIOUaeiou'
        vowel_count = 0
        consonant_count = 0
        for char in word:
            if not (char.isdigit() or char.isalpha()):
                return False
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        return (vowel_count > 0) and (consonant_count > 0)