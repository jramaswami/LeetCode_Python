"""
LeetCode
2981. Find Longest Special Substring That Occurs Thrice I
December 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def maximumLength(self, s: str) -> int:
        soln = -1
        for window_size in range(1, len(s)):
            window = collections.deque()
            freqs = collections.Counter()
            specials_seen = collections.defaultdict(int)
            for c in s:
                freqs[c] += 1
                window.append(c)
                while len(window) > window_size:
                    x = window.popleft()
                    freqs[x] -= 1
                    if freqs[x] == 0:
                        del freqs[x]
                if len(window) == window_size and len(freqs) == 1:
                    specials_seen[window[0]] += 1
            
            if any(t >= 3 for t in specials_seen.values()):
                soln = max(soln, window_size)
        return soln
