"""
LeetCode
2942. Find Words Containing Character
May 2025 Challenge
jramaswami
"""


from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, wd in enumerate(words) if x in wd]