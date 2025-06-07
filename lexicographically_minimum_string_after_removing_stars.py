"""
LeetCode
3170. Lexicographically Minimum String After Removing Stars
June 2025 Challenge
jramaswami
"""


import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        t = list(s)
        h = []
        for curr_index, curr_char in enumerate(s):
            if curr_char == '*':
                prev_char, neg_prev_index = heapq.heappop(h)
                t[-neg_prev_index] = '*'
            else:
                heapq.heappush(h, (curr_char, -curr_index))
        return ''.join(char for char in t if char != '*')