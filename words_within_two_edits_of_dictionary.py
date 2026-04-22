"""
LeetCode
2452. Words Within Two Edits of Dictionary
April 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        soln = []
        for word in queries:
            for target in dictionary:
                d = sum(x != y for x, y in zip(word, target))
                if d <= 2:
                    soln.append(word)
                    break
        return soln