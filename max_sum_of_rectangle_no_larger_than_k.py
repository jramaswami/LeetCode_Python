"""
LeetCode :: June 2021 Challenge :: Max Sum of Rectangle No Larger Than K
jramaswami
"""


from itertools import accumulate
from math import inf


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        prefix = [[0 for _ in row] for row in matrix]

        def get(r, c):
            result = 0
            if r >= 0 and c >= 0:
                result = prefix[r][c]
            return result

        def get_sum(tlr, tlc, brr, brc):
            return (get(brr, brc) - get(brr, tlc - 1) - get(tlr - 1, brc)
                    + get(tlr - 1, tlc - 1))

        # Compute prefix sums for the matrix.
        # O(N^2)
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                prefix[r][c] = v + get(r-1, c) + get(r, c-1) - get(r-1, c-1)

        # Search matrix for best solution.
        # O(N^4)
        soln = -inf
        N = len(matrix)
        M = len(matrix[0])
        for tlr in range(N):
            for tlc in range(M):
                for brr in range(tlr, N):
                    for brc in range(tlc, M):
                        S = get_sum(tlr, tlc, brr, brc)
                        if S <= k:
                            soln = max(soln, S)

        return soln


def test_1():
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    expected = 2
    assert Solution().maxSumSubmatrix(matrix, k) == expected


def test_2():
    matrix = [[2,2,-1]]
    k = 3
    expected = 3
    assert Solution().maxSumSubmatrix(matrix, k) == expected


def test_3():
    matrix = [[37, -60, 85, -41, -57, 30, -96, -50, -97, 75, 59, -27, 49, 97, -55, -51, -8, 94, 43, 22], [30, -20, 50, -54, 75, -61, 5, 55, -69, -24, -50, 44, 93, -97, -90, -53, 18, 78, 3, -85], [23, -50, -20, -98, 26, 79, -12, 6, 57, -82, -4, -20, -47, -34, 76, 47, 0, -97, -77, -73], [-18, -90, -33, 44, -50, -54, -60, -76, 92, 4, 73, 77, 89, -17, 60, 58, -78, -77, -53, -47], [4, -33, 90, -83, -53, -50, -83, 10, -12, 14, -17, 29, 25, -19, -27, 93, 51, -39, 24, -15], [-98, -6, -50, 13, 65, 59, 64, 2, 9, 67, -50, -51, 39, 66, -99, 84, 8, 68, -43, 96], [13, -3, 15, -26, -11, 31, -50, 83, -20, 94, -16, -72, 34, 48, -13, -51, 24, 66, -54, -71], [37, 25, 70, -14, 2, -20, -77, -3, 29, 30, -65, 81, -80, -65, -56, 20, -65, 90, 13, -46], [63, -20, 48, -27, -56, 8, 100, -50, -72, -20, 74, -90, -77, -15, 32, 67, -18, -75, 27, -70], [-45, -5, 55, -26, -16, -87, 92, 7, 74, 26, -23, 13, -69, 57, -76, 11, -99, 76, -86, 11], [23, -46, 63, 67, 25, 78, 13, 7, -43, 91, -70, -84, -30, -74, -34, -74, -32, 43, -32, -84], [-47, 37, 64, -42, -62, -60, 54, 19, -53, -47, 73, 43, -65, -11, 64, -46, 2, 47, -83, 95], [-49, -90, 94, 23, -64, 75, -68, -64, 43, -79, 0, 58, -58, -39, 93, -93, -19, 30, -47, 95], [-84, 91, 58, 42, 99, -31, 74, 62, -18, -48, 53, 53, 8, 84, -43, 0, -55, -63, 52, 97], [-46, 38, 65, -94, -46, -92, -25, -34, -74, -99, -90, 22, -29, -45, -50, -25, -84, 88, 67, -2], [-60, -93, 2, 16, -15, 50, 100, -8, -17, 61, -75, -1, 30, 10, 34, -38, -21, 51, -91, 35], [26, -40, 29, 42, 99, -20, -87, 29, 49, 1, 67, 4, 60, -81, -97, 14, 38, -37, -16, -24], [-42, 63, -20, 81, 43, 73, -79, -40, -31, -75, 32, 51, 48, -54, 28, -21, 93, -31, 79, -29], [-44, -91, 53, 52, 12, -18, -94, -40, 98, 20, 95, -27, 0, -74, 20, 25, 74, -42, -39, 59], [-19, -6, -87, -95, -61, -85, -60, 28, -9, -81, 60, 89, 91, -66, -10, -67, 33, 17, -74, -60]]
    k = 1000
    expected = 796
    for row in matrix:
        print(matrix)
    assert Solution().maxSumSubmatrix(matrix, k) == expected
