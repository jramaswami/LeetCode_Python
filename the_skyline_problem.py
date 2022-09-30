"""
LeetCode :: September 2022 Challenge :: The Skyline Problem
jramaswami
"""


import heapq
import collections


START = 1
STOP = -1


Event = collections.namedtuple('Event', ['type', 'index'])


class HeapItem:

    def __init__(self, height, start, stop):
        self.height = height
        self.start = start
        self.stop = stop

    def __lt__(self, other):
        "For heap, we put larger heights as less and first start less in a tie."
        if self.height == other.height:
            return self.end < other.end
        return self.height > other.height

    def __repr__(self):
        return f"HeapItem(height={self.height}, start={self.start}, stop={self.stop})"


class PQ:

    def __init__(self):
        self.heap = []

    def top(self):
        if self.heap:
            return self.heap[0]

    def push(self, start, stop, height):
        heapq.heappush(self.heap, HeapItem(height, start, stop))

    def pop(self):
        x = self.heap[0]
        heapq.heappop(self.heap)
        return x

    def __len__(self):
        return len(self.heap)


class Solution:

    def getSkyline(self, buildings):
        # Create as a stream of events.
        events = collections.defaultdict(list)
        for index, (start, stop, _) in enumerate(buildings):
            events[start].append(Event(START, index))
            events[stop].append(Event(STOP, index))

        # Process the stream of events.
        soln = []
        pq = PQ()
        for curr_time in sorted(events):
            # Remove any expired items for the current time.
            while pq and pq.top().stop <= curr_time:
                pq.pop()
            # Add new items, if there are any.
            for event in events[curr_time]:
                if event.type == START:
                    pq.push(*buildings[event.index])

            # Did the height change?
            if not pq:
                soln.append([curr_time, 0])
            elif not soln or pq.top().height != soln[-1][1]:
                soln.append([curr_time, pq.top().height])
        return soln


def test_1():
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    expected = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    assert Solution().getSkyline(buildings) == expected


def test_2():
    buildings = [[0,2,3],[2,5,3]]
    expected = [[0,3],[5,0]]
    assert Solution().getSkyline(buildings) == expected


def test_3():
    "RTE"
    buildings = [[0,3,3],[1,5,3],[2,4,3],[3,7,3]]
    expected = [[0,3],[5,0]]
    assert Solution().getSkyline(buildings) == expected