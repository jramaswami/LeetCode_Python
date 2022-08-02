"""
LeetCode :: August 2022 Challenge :: Kth Smallest Element in a Sorted Matrix
jramaswami
"""


class Solution:
    def kthSmallest(self, matrix, k):
        r = 0
        c = len(matrix[0]) - 1
        n = len(matrix[0])
        while n != k:
            if n > k:
                c -= 1
                n -= 1
            elif n < k:
                r += 1
                n += (c + 1)
        return matrix[r][c]


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