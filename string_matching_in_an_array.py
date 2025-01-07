"""
LeetCode
1408. String Matching in an Array
January 2025 Challenge
jramaswami
"""


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        soln = []
        for i, wd_a in enumerate(words):
            for wd_b in words[i+1:]:
                if wd_a in wd_b:
                    soln.append(wd_a)
                    break
        return soln
