"""
LeetCode
2901. Longest Unequal Adjacent Groups Subsequence II
May 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming_distance(wd1, wd2):
            return sum(1 if a != b else 0 for a, b in zip(wd1, wd2))

        longest_subsequence = [1 for _ in words]
        parent = [None for _ in words]
        soln_tail = 0
        current_longest = 1
        for i, wd1 in enumerate(words):
            g1 = groups[i]
            for j, wd2 in enumerate(words[:i]):
                g2 = groups[j]
                if g1 != g2 and len(wd1) == len(wd2) and hamming_distance(wd1, wd2) == 1:
                    if longest_subsequence[j] + 1 > longest_subsequence[i]:
                        parent[i] = j
                        longest_subsequence[i] = longest_subsequence[j] + 1
                    if longest_subsequence[i] > current_longest:
                        current_longest = longest_subsequence[i]
                        soln_tail = i

        # Reconstruct
        i = soln_tail
        soln = [words[i]]
        while parent[i] is not None:
            i = parent[i]
            soln.append(words[i])
        return soln[::-1]