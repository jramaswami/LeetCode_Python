"""
LeetCode
1792. Maximum Average Pass Ratio
December 2024 Challenge
jramaswami
"""


import dataclasses
import heapq


class MaxPQ:
    def __init__(self):
        self.heap = []

    def push(self, priority, item):
        heapq.heappush(self.heap, (-priority, item))
    
    def pop(self):
        _, item = heapq.heappop(self.heap)
        return item

    def top(self):
        _, item = self.heap[0]
        return item


@dataclasses.dataclass
class SchoolClass:
    passed: int
    total: int

    def curr_average(self):
        return self.passed / self.total

    def next_average(self):
        return (self.passed + 1) / (self.total + 1)

    def __lt__(self, other):
        return self.total < other.total


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_pq = MaxPQ()
        for p, t in classes:
            school_class = SchoolClass(p, t)
            priority = school_class.next_average() - school_class.curr_average()
            max_pq.push(priority, school_class)
        for _ in range(extraStudents):
            school_class = max_pq.pop()
            school_class.passed += 1
            school_class.total += 1
            priority = school_class.next_average() - school_class.curr_average()
            max_pq.push(priority, school_class)
        return sum(sc[1].curr_average() for sc in max_pq.heap) / len(max_pq.heap)
