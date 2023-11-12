"""
LeetCode
815. Bus Routes
November 2023 Challenge
jramaswami
"""


from typing import List
import collections


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Corner case
        if source == target:
            return 0

        graph = collections.defaultdict(list)
        target_bus = -1
        source_bus = -1
        for bus_number_u, bus_stops_u in enumerate(routes):
            if target in bus_stops_u:
                target_bus = bus_number_u
            if source in bus_stops_u:
                source_bus = bus_number_u
            for bus_number_v, bus_stops_v in enumerate(routes[bus_number_u+1:], start=bus_number_u+1):
                if any(u in bus_stops_v for u in bus_stops_u):
                    graph[bus_number_u].append(bus_number_v)
                    graph[bus_number_v].append(bus_number_u)

        queue = collections.deque()
        queue.append((source_bus, 1))
        visited = set()
        while queue:
            u, d = queue.popleft()
            if u == target_bus:
                return d
            for v in graph[u]:
                if v not in visited:
                    queue.append((v, d+1))
                    visited.add(v)
        return -1


def test_1():
    routes = [[1,2,7],[34,6,7]]
    source = 1
    target = 6
    expected = 2
    assert Solution().numBusesToDestination(routes, source, target) == expected


def test_2():
    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
    expected = -1
    assert Solution().numBusesToDestination(routes, source, target) == expected


def test_3():
    "WA"
    routes = [[1,7],[3,5]]
    source = 5
    target = 5
    expected = 0
    assert Solution().numBusesToDestination(routes, source, target) == expected


def test_4():
    "WA"
    routes = [[16,25,29,35,42],[32],[1],[1,2,5,17,22,34,38,41,44],[1,16,23,24,32,36,38,45],[9,11,43],[5,10,15,22,27,38],[7,8,14,19,22,23,25,26,27],[3,8,24,29,47,48],[4,16,18,25,36,41]]
    source = 17
    target = 38
    expected = 1
    assert Solution().numBusesToDestination(routes, source, target) == expected