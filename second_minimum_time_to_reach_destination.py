"""
LeetCode
2045. Second Minimum Time to Reach Destination
July 2024 Challenge
jramaswami

Thank You NeetCode!
"""


import collections
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Convert to graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = [1]
        new_queue = []
        curr_time = 0
        res = -1
        visit_times = collections.defaultdict(list)
        while queue:
            for u in queue:
                if u == n:
                    if res != -1:
                        return curr_time
                    res = curr_time
                for v in graph[u]:
                    neighbor_times = visit_times[v]
                    if len(neighbor_times) == 0 or (len(neighbor_times) == 1 and neighbor_times[0] != curr_time):
                        new_queue.append(v)
                        neighbor_times.append(curr_time)

            if (curr_time // change) % 2 == 1:
                curr_time += change - (curr_time % change)
            curr_time += time
            queue, new_queue = new_queue, []



def test_1():
    n = 5
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    time = 3
    change = 5
    expected = 13
    assert Solution().secondMinimum(n, edges, time, change) == expected


def test_2():
    n = 2
    edges = [[1,2]]
    time = 3
    change = 2
    expected = 11
    assert Solution().secondMinimum(n, edges, time, change) == expected