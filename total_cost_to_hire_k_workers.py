"""
LeetCode
2462. Total Cost to Hire K Workers
June 2023 Challenge
jramaswami
"""


import heapq
import collections
from typing import List


Candidate = collections.namedtuple('Candidate', ['cost', 'index'])


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Use a deque for convenience
        costs0 = collections.deque(Candidate(c, i) for i, c in enumerate(costs))
        # Initialize with first/last candidates
        left_candidates = []
        right_candidates = []
        while costs0 and len(left_candidates) < candidates:
            heapq.heappush(left_candidates, costs0.popleft())
        while costs0 and len(right_candidates) < candidates:
            heapq.heappush(right_candidates, costs0.pop())

        total_cost = 0
        for _ in range(k):
            if not left_candidates:
                total_cost += right_candidates[0].cost
                heapq.heappop(right_candidates)
                if costs0:
                    heapq.heappush(right_candidates, costs0.pop())
            elif not right_candidates:
                total_cost += left_candidates[0].cost
                heapq.heappop(left_candidates)
                if costs0:
                    heapq.heappush(left_candidates, costs0.popleft())
            elif left_candidates[0].cost <= right_candidates[0].cost:
                total_cost += left_candidates[0].cost
                heapq.heappop(left_candidates)
                if costs0:
                    heapq.heappush(left_candidates, costs0.popleft())
            else:
                total_cost += right_candidates[0].cost
                heapq.heappop(right_candidates)
                if costs0:
                    heapq.heappush(right_candidates, costs0.pop())
        return total_cost


def test_1():
    costs = [17,12,10,2,7,2,11,20,8]
    k = 3
    candidates = 4
    expected = 11
    assert Solution().totalCost(costs, k, candidates) == expected


def test_2():
    costs = [1,2,4,1]
    k = 3
    candidates = 3
    expected = 4
    assert Solution().totalCost(costs, k, candidates) == expected
