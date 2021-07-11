"""
LeetCode :: July 2021 Challenge :: Find Median from Data Stream
jramaswami
"""


import heapq


class PriorityQueue:
    """
    Convenience class to simulate both a min and max priority queue.
    Python's heapq is a min heap, so for a max priority queue we can multiply by -1.
    """
    def __init__(self, coefficient=1):
        self.coefficient = coefficient
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, self.coefficient * value)

    def pop(self):
        return self.coefficient * heapq.heappop(self.heap)

    def peek(self):
        return self.coefficient * self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str([self.coefficient * h for h in self.heap])


class MedianFinder:

    def __init__(self):
        self.left = PriorityQueue(-1)
        self.right = PriorityQueue(1)
        self.current_median = None

    def addNum(self, num):
        # Add number
        if self.current_median is None or num < self.findMedian():
            self.left.push(num)
        else:
            self.right.push(num)


        # Balance queues
        total_items = len(self.left) + len(self.right)
        balance = total_items % 2
        while abs(len(self.left) - len(self.right)) > balance:
            if len(self.left) > len(self.right):
                k = self.left.pop()
                self.right.push(k)
            elif len(self.right) > len(self.left):
                k = self.right.pop()
                self.left.push(k)

        # Compute median
        if total_items % 2:
            if len(self.left) > len(self.right):
                self.current_median = self.left.peek()
            else:
                self.current_median = self.right.peek()
        else:
            self.current_median = (self.left.peek() + self.right.peek()) / 2

    def findMedian(self):
        return self.current_median


#
# Testing
#


null = None


def test_1():
    meths = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
    args = [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
    expected = [null,null,6.00000,null,8.00000,null,6.00000,null,6.00000,null,6.00000,null,5.50000,null,6.00000,null,5.50000,null,5.00000,null,4.00000,null,3.00000]

    MF = MedianFinder()
    for (m, a, e) in zip(meths[1:], args[1:], expected[1:]):
        r = getattr(MF, m)(*a)
        assert r == e
