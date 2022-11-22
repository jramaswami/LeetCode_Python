"""
LeetCode :: October 2021 Challenge :: 279. Perfect Squares
jramaswami
"""


class Solution:
    def numSquares(self, n):
        k = 1
        perfect_squares = []
        while k * k <= n:
            perfect_squares.append(k * k)
            k += 1


        queue = set(perfect_squares)
        new_queue = set()
        soln = 1
        while queue:
            for k in queue:
                if k == n:
                    return soln
                for p in perfect_squares:
                    if p + k > n:
                        break
                    new_queue.add(p + k)

            queue, new_queue = new_queue, set()
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


def test_6():
    "TLE"
    n = 3258
    assert Solution().numSquares(n) == 2
