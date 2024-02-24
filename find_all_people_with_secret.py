"""
LeetCode
2092. Find All People With Secret
February 2024
jramaswami
"""


import collections
from typing import List


Edge = collections.namedtuple('Edge', ['dest', 'time'])
QItem = collections.namedtuple('QItem', ['source', 'time'])


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Transform meetings into graph with timed edges
        graph = [[] for _ in range(n)]
        for u, v, t in meetings:
            graph[u].append(Edge(v,t))
            graph[v].append(Edge(u,t))

        has_secret = [False for _ in range(n)]
        has_secret[0] = True
        has_secret[firstPerson] = True
        queue = collections.deque()
        queue.append(QItem(firstPerson, 0))
        while queue:
            item = queue.popleft()
            for edge in graph[item.source]:
                if item.time <= edge.time and not has_secret[edge.dest]:
                    print(item, edge)
                    has_secret[edge.dest] = True
                    queue.append(QItem(edge.dest, edge.time))

        return [i for i, s in enumerate(has_secret) if s]


def test_1():
    n = 6
    meetings = [[1,2,5],[2,3,8],[1,5,10]]
    firstPerson = 1
    expected = [0,1,2,3,5]
    assert Solution().findAllPeople(n, meetings, firstPerson) == expected


def test_2():
    n = 4
    meetings = [[3,1,3],[1,2,2],[0,3,3]]
    firstPerson = 3
    expected = [0,1,3]
    assert Solution().findAllPeople(n, meetings, firstPerson) == expected


def test_3():
    n = 5
    meetings = [[3,4,2],[1,2,1],[2,3,1]]
    firstPerson = 1
    expected = [0,1,2,3,4]
    assert Solution().findAllPeople(n, meetings, firstPerson) == expected


def test_4():
    "WA"
    n = 6
    meetings = [[0,2,1],[1,3,1],[4,5,1]]
    firstPerson = 1
    expected = [0,1,2,3]
    assert Solution().findAllPeople(n, meetings, firstPerson) == expected