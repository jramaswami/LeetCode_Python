"""
LeetCode
214. Shortest Palindrome
September 2024 Challenge
jramaswami
Thank You NeetCodeIO!
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return s

        MOD = pow(10, 9) + 1
        base = 29
        suffix = 0
        prefix = 0
        m = 1
        max_i = -1
        for i, c in enumerate(s):
            x = ord(c) - ord('a') + 1
            prefix = (base * prefix) % MOD
            prefix = (prefix + x) % MOD
            
            suffix = (suffix + x * m) % MOD
            m = (m * base) % MOD

            if suffix == prefix:
                max_i = i
        return s[max_i+1:][::-1] + s
