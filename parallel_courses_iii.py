"""
LeetCode
2050. Parallel Courses III
October 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        inDegree = [0 for _ in time]
        graph = [[] for _ in time]
        for u, v in relations:
            inDegree[v-1] += 1
            graph[u-1].append(v-1)

        timeToComplete = [0 for _ in time]
        queue = collections.deque()
        for u, d in enumerate(inDegree):
            if d == 0:
                queue.append(u)
                timeToComplete[u] = time[u]

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                timeToComplete[v] = max(timeToComplete[v], time[v] + timeToComplete[u])
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.append(v)

        return max(timeToComplete)


def test_1():
    n = 3
    relations = [[1,3],[2,3]]
    time = [3,2,5]
    expected = 8
    assert Solution().minimumTime(n, relations, time) == expected


def test_2():
    n = 5
    relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
    time = [1,2,3,4,5]
    expected = 12
    assert Solution().minimumTime(n, relations, time) == expected