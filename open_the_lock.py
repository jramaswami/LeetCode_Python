"""
LeetCode :: June 2021 Challenge :: Open the Lock
jramaswami
"""


from typing import *
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends0 = set(deadends)
        visited = set()
        queue = deque()

        def enqueue(combo, turns):
            """
            Only enqueue a combination if it is not in deadends and has not
            been visited.
            """
            if combo in deadends0 or combo in visited:
                return
            visited.add(combo)
            queue.append((combo, turns))


        def neighbors(combo):
            """Return all the possible neighbors of this combo"""
            result = []
            combo0 = [int(i) for i in combo]
            for i, n in enumerate(combo0):
                # Add 1
                if n == 9:
                    n1 = 0
                else:
                    n1 = n + 1
                combo1 = "".join(str(n1) if j == i else str(k) for j, k in enumerate(combo0))
                result.append(combo1)
                # Sub 1
                if n == 0:
                    n1 = 9
                else:
                    n1 = n - 1
                combo2 = "".join(str(n1) if j == i else str(k) for j, k in enumerate(combo0))
                result.append(combo2)
            return result


        enqueue("0000", 0)
        while queue:
            combo, turns = queue.popleft()
            if combo == target:
                return turns
            for combo1 in neighbors(combo):
                enqueue(combo1, turns + 1)
        return -1


def test_1():
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    assert Solution().openLock(deadends, target) == 6


def test_2():
    deadends = ["8888"]
    target = "0009"
    assert Solution().openLock(deadends, target) == 1


def test_3():
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    assert Solution().openLock(deadends, target) == -1


def test_4():
    deadends = ["0000"]
    target = "8888"
    assert Solution().openLock(deadends, target) == -1
