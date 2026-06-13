"""
LeetCode
3838. Weighted Word Mapping
June 2026 Challenge
jramaswami
"""


import string


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        MOD = 26

        def word_weight(word):
            weight = 0
            for letter in word:
                index = ord(letter) - ord('a')
                weight += weights[index]
                weight %= MOD
            return weight % MOD

        reversed_letters = list(reversed(string.ascii_lowercase))
        word_weights = [word_weight(word) for word in words]
        return ''.join(reversed_letters[wt] for wt in word_weights)