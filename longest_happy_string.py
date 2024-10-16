"""
LeetCode
1405. Longest Happy String
October 2024 Challenge
jramawami
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freqs = [[a, 'a'], [b, 'b'], [c, 'c']]
        soln = []
        while 1:
            freqs.sort()
            i = -1
            if len(soln) > 1 and soln[-1] == freqs[-1][1] and soln[-2] == freqs[-1][1]:
                i = -2
            if freqs[i][0] == 0:
                break
            freqs[i][0] -= 1
            soln.append(freqs[i][1])
        return ''.join(soln)
