"""
LeetCode
2073. Time Needed to Buy Tickets
April 2024 Challenge
jramaswami
"""

import collections
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        Q = collections.deque((i, t) for i, t in enumerate(tickets))
        result = [0 for _ in tickets]
        timer = 0
        while Q:
            i, t = Q.popleft()
            timer += 1
            if t - 1 > 0:
                Q.append((i, t-1))
            else:
                if i == k:
                    return timer