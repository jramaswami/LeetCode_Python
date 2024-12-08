"""
LeetCode
2054. Two Best Non-Overlapping Events
December 2024 Challenge
jramaswami
"""


import collections
import heapq


START = -1
STOP = 1


Event = collections.namedtuple('Event', ['time', 'type', 'value'])


class MaxPQ:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        priority = -item.value
        heapq.heappush(self.heap, (priority, item))
    
    def top(self):
        return self.heap[0][1]

    def __len__(self):
        return len(self.heap)


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events0 = []
        for start, stop, value in events:
            events0.append(Event(start, START, value))
            events0.append(Event(stop, STOP, value))
        events0.sort()
        past_events = MaxPQ()
        soln = max(event.value for event in events0)
        for event in events0:
            if event.type == STOP:
                past_events.push(event)
            else:
                if past_events:
                    soln = max(event.value + past_events.top().value, soln)
        
        return soln
