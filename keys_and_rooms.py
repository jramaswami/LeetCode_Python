"""
LeetCode :: March 2021 Challenge :: Keys and Rooms
jramaswami
"""
from typing import *
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keychain = set()
        keychain.add(0)
        queue = deque()
        queue.append(0)
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in keychain:
                    keychain.add(key)
                    queue.append(key)
        return len(keychain) == len(rooms)


def test_1():
    assert Solution().canVisitAllRooms([[1],[2],[3],[]]) == True

def test_2():
    assert Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False
