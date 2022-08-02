"""
LeetCode :: August 2022 Challenge :: Kth Smallest Element in a Sorted Matrix
jramaswami
"""


import heapq


class Solution:
    def kthSmallest(self, matrix, k):
        i = 0
        H = [(matrix[0][0], 0, 0)]
        curr = None
        while i < k:
            i += 1
            curr, r, c = heapq.heappop(H)
            if r + 1 < len(matrix):
                heapq.heappush(H, (matrix[r+1][c], r+1, c))
            if c + 1 < len(matrix[r]):
                heapq.heappush(H, (matrix[r][c+1], r, c+1))
        return curr


def test_1():
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    expected = 13
    assert Solution().kthSmallest(matrix, k) == expected


def test_2():
    matrix = [[-5]]
    k = 1
    expected = -5
    assert Solution().kthSmallest(matrix, k) == expected


def test_3():
    "WA"
    matrix = [[1, 2], [1, 3]]
    k = 2
    expected = 1
    assert Solution().kthSmallest(matrix, k) == expected


def test_4():
    matrix = [[1,3,5],[6,7,12],[11,14,14]]
    k = 6
    expected = 11
    assert Solution().kthSmallest(matrix, k) == expected