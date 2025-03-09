"""
LeetCode
3208. Alternating Groups II
March 2025 Challenge
jramaswami
"""


import collections
import dataclasses
import itertools


@dataclasses.dataclass
class WindowItem:
    color: int
    same_as_next: bool
    index: int


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        window = collections.deque()
        curr_same_as_next = 0
        N = len(colors)
        soln = 0
        for i in range(0, N+k-1):
            color = colors[i % N]
            curr_item = WindowItem(color, False, i)
            # Update if previous item is same color as current item
            if window:
                prev_item = window[-1]
                if prev_item.color == curr_item.color:
                    prev_item.same_as_next = True
                    curr_same_as_next += 1
            # Add item to queue
            window.append(curr_item)
            # Reduce window to size k, adjusting curr_same_as_next
            while len(window) > k:
                rem_item = window.popleft()
                if rem_item.same_as_next:
                    curr_same_as_next -= 1
            # Count
            if len(window) == k and curr_same_as_next == 0:
                soln += 1
        return soln    
