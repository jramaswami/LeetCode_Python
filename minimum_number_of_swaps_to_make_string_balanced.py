"""
LeetCode
1963. Minimum Number of Swaps to Make the String Balanced
October 2024 Challenge
jramaswami
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        openings = [i for i, c in enumerate(s) if c == '[']
        t = list(s)
        swaps = 0
        openers = 0
        closers = 0
        for i in range(len(t)):
            if t[i] == '[':
                openers += 1
            elif t[i] == ']':
                closers += 1
                if closers > openers:
                    j = openings.pop()
                    t[i], t[j] = t[j], t[i]
                    closers -= 1
                    openers += 1
                    swaps += 1
        return swaps
