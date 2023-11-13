"""
LeetCode
2785. Sort Vowels in a String
November 2023 Challenge
jramaswami
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        t = []
        v = []
        for c in s:
            if c.lower() in 'aeiou':
                v.append(c)
                t.append('*')
            else:
                t.append(c)

        v.sort(key=lambda c: ord(c))
        i = 0
        for j, c in enumerate(t):
            if c == '*':
                t[j] = v[i]
                i += 1
        return "".join(t)