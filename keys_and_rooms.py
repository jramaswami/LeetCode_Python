"""
LeetCode
Keys and Rooms
December 2022 Challenge
jramaswami
"""


from typing import *
import collections


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = collections.deque()
        visited = [False for _ in rooms]
        visited[0] = True
        queue.append(0)
        while queue:
            r = queue.popleft()
            for p in rooms[r]:
                if not visited[p]:
                    visited[p] = True
                    queue.append(p)
        return all(visited)


def test_1():
    assert Solution().canVisitAllRooms([[1],[2],[3],[]]) == True

def test_2():
    assert Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False
