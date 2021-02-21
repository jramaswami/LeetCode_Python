"""
LeetCode :: Broken Calculator
jramaswami
"""
from collections import deque
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        visited = set()
        queue = deque()
        queue.append((X, 0))
        visited.add(X)
        while queue:
            X0, ops = queue.popleft()
            if X0 == Y:
                return ops
            if X0 < Y and X0 * 2 not in visited:
                if X0 * 2 == Y:
                    return ops + 1
                queue.append((X0 * 2, ops + 1))
                visited.add(X0 * 2)
            if X0 > 0 and X0 - 1 not in visited:
                if X0 - 1 == Y:
                    return ops + 1
                queue.append((X0 - 1, ops + 1))
                visited.add(X0 - 1)

def test_1():
    assert Solution().brokenCalc(2, 3) == 2

def test_2():
    assert Solution().brokenCalc(5, 8) == 2

def test_3():
    assert Solution().brokenCalc(3, 10) == 3

def test_4():
    assert Solution().brokenCalc(1024, 1) == 1023
