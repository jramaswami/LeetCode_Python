"""
LeetCode :: October 2021 Challenge :: 279. Perfect Squares
jramaswami
"""


import collections
import heapq


QItem = collections.namedtuple('QItem', ['items', 'sum'])


class Solution:

    def __init__(self):
        # Cache the squares up to the maximum n.
        max_n = pow(10, 4)
        self.squares = []
        for k in range(1, max_n):
            sq = k * k
            if sq > max_n:
                break
            self.squares.append(sq)


    def numSquares(self, n):
        useful_squares = [k for k in self.squares if k <= n]
        Q = [QItem(1, k) for k in useful_squares]
        while Q:
            item = heapq.heappop(Q)
            if item.sum == n:
                return item.items

            for k in useful_squares:
                if item.sum + k > n:
                    break
                heapq.heappush(Q, QItem(item.items + 1, item.sum + k))


def test_1():
    assert Solution().numSquares(12) == 3


def test_2():
    assert Solution().numSquares(13) == 2


def test_3():
    """TLE"""
    assert Solution().numSquares(351) == 4
