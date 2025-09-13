"""
LeetCode
3541. Find Most Frequent Vowel and Consonant
September 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def maxFreqSum(self, s: str) -> int:
        freqs = collections.Counter(s)
        vowels = 'aeiou'
        max_vowel_freq = max_consonant_freq = 0
        for char, freq in freqs.items():
            if char in vowels:
                max_vowel_freq = max(max_vowel_freq, freq)
            else:
                max_consonant_freq = max(max_consonant_freq, freq)
        return max_vowel_freq + max_consonant_freq
