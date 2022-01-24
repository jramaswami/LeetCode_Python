"""
LeetCode :: January 2022 Challenge :: 520. Detect Capital
jramaswami
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (all(c.isupper() for c in word) or
                all(c.islower() for c in word) or
                (word[0].isupper() and all(c.islower() for c in word[1:]))
       )
