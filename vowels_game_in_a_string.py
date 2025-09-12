"""
LeetCode
3227. Vowels Game in a String
September 2025 Challenge
jramaswami
"""


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        vowel_count = sum(1 if c in vowels else 0 for c in s)
        if vowel_count == 0:
            return False
        return True
