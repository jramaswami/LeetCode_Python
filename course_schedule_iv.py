"""
LeetCode
1462. Course Schedule IV
January 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reverse_graph = collections.defaultdict(list)
        for prq, crs in prerequisites:
            reverse_graph[crs].append(prq)

        prqs_lookup = collections.defaultdict(set)

        def query(prq, crs):
            if crs not in prqs_lookup:
                visited = set()
                visted.add(crs)
                queue = collections.deque()
                queue.append(crs)
                while queue:
                    u = queue.popleft()
                    if u != crs:
                        prqs_lookup[crs].add(u)
                    for v in reverse_graph[u]:
                        if v not in visited:
                            visited.add(v)
                            queue.append(v)
            return prq in prqs_lookup[crs]

        return [query(prq, crs) for prq, crs in queries]


def test_1():
    numCourses = 2
    prerequisites = [[1,0]]
    queries = [[0,1],[1,0]]
    expected = [False,True]
    assert Solution().checkIfPrerequisite(numCourses, prerequisites, queries) == expected


def test_2():
    numCourses = 2
    prerequisites = []
    queries = [[1,0],[0,1]]
    expected = [False,False]
    assert Solution().checkIfPrerequisite(numCourses, prerequisites, queries) == expected


def test_3():
    numCourses = 3
    prerequisites = [[1,2],[1,0],[2,0]]
    queries = [[1,0],[1,2]]
    expected = [True,True]
    assert Solution().checkIfPrerequisite(numCourses, prerequisites, queries) == expected
