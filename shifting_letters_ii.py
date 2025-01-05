"""
LeetCode
2381. Shifting Letters II
January 2025 Challenge
jramaswami
"""


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0 for _ in s]
        for left, right, dirn in shifts:
            if dirn == 0:
                dirn = -1
            prefix[left] += dirn
            if right + 1 < len(s):
                prefix[right+1] -= dirn
        
        soln = []
        curr_shift = 0
        ord_a = ord('a')
        for c, p in zip(s, prefix):
            x = ord(c) - ord_a
            curr_shift += p
            y = (curr_shift + 26 + x) % 26
            soln.append(chr(ord_a + y))
        return ''.join(soln)
