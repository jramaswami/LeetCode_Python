"""
LeetCode
2416. Sum of Prefix Scores of Strings
September 2024 Challenge
jramaswami
Thank You NeetCodeIO!
"""


import collections


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        count = collections.defaultdict(int)
        for w in words:
            for i in range(len(w)):
                count[w[:i+1]] += 1

        soln = []
        for w in words:
            score = 0
            for i in range(len(w)):
                score += count[w[:i+1]]
            soln.append(score)
        return soln
