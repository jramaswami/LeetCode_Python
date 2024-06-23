"""
LeetCode
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
June 2024 Challenge
jramaswami
"""


import collections
import heapq


QItem = collections.namedtuple('QItem', ['value', 'index'])


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        soln = 0
        min_queue = []
        max_queue = []
        window = collections.deque()
        for i, n in enumerate(nums):
            # Add current item to window and min/max queues
            window.append(QItem(n, i))
            heapq.heappush(min_queue, QItem(n, i))
            heapq.heappush(max_queue, QItem(-n, i))

            # While the window has items that are two far from each other
            while (-max_queue[0].value) - min_queue[0].value > limit:
                # Remove leftmost item from window
                window.popleft()
                # Remove any items from min/max queues that are to the left of
                # the current window
                while min_queue[0].index < window[0].index:
                    heapq.heappop(min_queue)
                while max_queue[0].index < window[0].index:
                    heapq.heappop(max_queue)
            soln = max(soln, len(window)) 
        return soln
