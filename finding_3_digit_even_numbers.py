"""
LeetCode
2094. Finding 3-Digit Even Numbers
May 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Since there are only ~ 10^3 even numbers we can look
        # at, iterate through those and dermine if each can be
        # made with the frequency of digits.
        soln = []
        freqs = collections.Counter(digits)
        for x in range(100, 1000, 2):
            xfreqs = collections.Counter(int(d) for d in str(x))
            if all(xfreqs[d] <= freqs[d] for d in xfreqs):
                soln.append(x)
        return soln