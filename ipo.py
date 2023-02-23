"""
LeetCode
502. IPO
February 2023
jramaswami
"""


from typing import *
import collections
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        all_projects = collections.deque(
            sorted([(-p, c) for p, c in zip(profits, capital)], key=lambda t: t[1])
        )
        avail_projects = []
        working_capital = w
        for _ in range(k):
            while all_projects and all_projects[0][1] <= working_capital:
                heapq.heappush(avail_projects, all_projects[0])
                all_projects.popleft()
            best_project = heapq.heappop(avail_projects)
            working_capital += -best_project[0]
        return working_capital


def test_1():
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,1]
    expected = 4
    assert Solution().findMaximizedCapital(k, w, profits, capital) == expected

def test_2():
    k = 3
    w = 0
    profits = [1,2,3]
    capital = [0,1,2]
    expected = 6
    assert Solution().findMaximizedCapital(k, w, profits, capital) == expected


def test_3():
    "RTE"
    k = 1
    w = 0
    profits = [1,2,3]
    capital = [1,1,2]
    assert Solution().findMaximizedCapital(k, w, profits, capital) == expected