"""
LeetCode
3330. Find the Original Typed String I
July 2025 Challenge
jramaswami
"""


class Solution:
    def possibleStringCount(self, word: str) -> int:
        t = [0]
        for a, b in zip(word, word[1:]):
            print(a, b)
            if a == b:
                t[-1] += 1
            else:
                t.append(0)
        return 1 + sum(t)