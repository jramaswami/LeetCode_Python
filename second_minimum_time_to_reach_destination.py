"""
LeetCode
2045. Second Minimum Time to Reach Destination
July 2024 Challenge
jramaswami
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

        INF = pow(10, 10)
        # Find shortest path from 1 to n.
        shortest_path = INF
        queue = collections.deque()
        queue.append((1, 0))
        visited = set()
        visited.add(1)
        while queue and shortest_path == INF:
            u, d = queue.popleft()
            if u == n:
                shortest_path = d
            else:
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v, d+1))

        # Find the next shortest path which will will
        # be shortest_path + 1 or shortest_path + 2 (cycle)
        # So, we can get by checking the existence of shortest_path + 1
        visited.clear()
        def dfs(u, d):
            visited.add(u)
            result = False

            if u == n and d == shortest_path + 1:
                result = True
            elif d >= shortest_path + 1:
                result = False
            else:
                for v in graph[u]:
                    if v not in visited:
                        if dfs(v, d+1):
                            result = True
                            break
            visited.remove(u)
            return result

        next_shortest_path = shortest_path + 2
        if dfs(1, 0):
            next_shortest_path = shortest_path + 1

        # Walk path with time out.
        curr_time = 0
        for i in range(1, next_shortest_path+1):
            if curr_time // change % 2 == 1:
                # We are in a closed time and cannot leave the current node.
                wait_time = curr_time % change
                curr_time = change * ((curr_time // change) + 1)
            curr_time += time
        return curr_time


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