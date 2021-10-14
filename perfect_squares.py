"""
LeetCode :: October 2021 Challenge :: 279. Perfect Squares
jramaswami
"""


class Solution:
    def numSquares(self, n):
        queue = [0]
        new_queue = []
        soln = 1
        while True:
            for j in queue:
                for k in range(1, n+1):
                    m = j + (k * k)
                    if m > n:
                        break

                    if m == n:
                        return soln
                    new_queue.append(m)
            queue, new_queue = new_queue, []
            soln += 1


def test_1():
    assert Solution().numSquares(12) == 3


def test_2():
    assert Solution().numSquares(13) == 2


def test_3():
    """TLE"""
    assert Solution().numSquares(351) == 4


def test_4():
    """TLE"""
    assert Solution().numSquares(4586) == 2


def test_5():
    """TLE"""
    assert Solution().numSquares(1) == 1
