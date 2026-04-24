"""
LeetCode
2833. Furthest Point From Origin
April 2026 Challenge
jramaswami
"""


import collections


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        freqs = collections.Counter(moves)
        return max(freqs['R'], freqs['L']) + freqs['_'] - min(freqs['R'], freqs['L'])