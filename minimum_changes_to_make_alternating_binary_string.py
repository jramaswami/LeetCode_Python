"""
LeetCode
1758. Minimum Changes To Make Alternating Binary String
December 2023 Challenge
jramaswami

The string is either 010101... or 1010101...
Count the how many are off for either of those
"""


class Solution:
    def minOperations(self, s: str) -> int:
        a = 0
        soln_a = 0
        soln_b = 0
        for c in s:
            if int(c) == a:
                soln_b += 1
            else:
                soln_a += 1
            a = (a + 1) % 2
        return min(soln_a, soln_b)