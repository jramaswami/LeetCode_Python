"""
LeetCode
207. Course Schedule
July 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            indegree[v] += 1
            graph[u].append(v)

        topo = []
        queue = collections.deque(i for i, d in enumerate(indegree) if d == 0)
        while queue:
            u = queue.popleft()
            topo.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return all(d == 0 for d in indegree)


def test_1():
    numCourses = 2
    prerequisites = [[1,0]]
    expected = True
    assert Solution().canFinish(numCourses, prerequisites) == expected

def test_2():
    numCourses = 2
    prerequisites = [[1,0], [0,1]]
    expected = False
    assert Solution().canFinish(numCourses, prerequisites) == expected