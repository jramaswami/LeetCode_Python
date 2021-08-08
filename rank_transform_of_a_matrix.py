"""
LeetCode :: August 2021 Challenge :: Rank Transform of a Matrix
jramaswami
"""


import math
import collections
import itertools


class UnionFind:

    def __init__(self):
        self.parent = dict()
        self.size = dict()
        self.rank = dict()

    def make_set(self, v):
        self.parent[v] = v
        self.size[v] = 1

    def find_set(self, v):
        if self.parent[v] == v:
            return v
        p = self.find_set(self.parent[v])
        self.parent[v] = p
        return p

    def union_set(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_rank(self, v, r):
        v = self.find_set(v)
        if v in self.rank:
            self.rank[v] = max(self.rank[v], r)
        else:
            self.rank[v] = r

    def get_rank(self, v):
        v = self.find_set(v)
        return self.rank[v]

    def has_rank(self, v):
        v = self.find_set(v)
        return v in self.rank


Element = collections.namedtuple('Element', ['row', 'col', 'val', 'rank'])

def row_generator(r, matrix, rank):
    """
    Generator that returns (row, col, value, rank) for every element in row.
    """
    for c, (mat_val, rank_val) in enumerate(zip(matrix[r], rank[r])):
        yield Element(r, c, mat_val, rank_val)

def col_generator(c, matrix, rank):
    """
    Generator that returns (row, col, value, rank) for every element in column.
    """
    for r, (mat_row, rank_row) in enumerate(zip(matrix, rank)):
        yield Element(r, c, mat_row[c], rank_row[c])

def max_ranked(row, col, matrix, rank):
    """
    Returns the element with the maximum rank in the row/colum.
    """
    curr_val = matrix[row][col]
    max_rank = -math.inf
    max_elem = None
    for elem in col_generator(col, matrix, rank):
        if elem.rank > max_rank:
            max_rank, max_elem = elem.rank, elem
        elif elem.rank == max_rank and elem.val < curr_val:
            max_rank, max_elem = elem.rank, elem
    for elem in row_generator(row, matrix, rank):
        if elem.rank > max_rank:
            max_rank, max_elem = elem.rank, elem
        elif elem.rank == max_rank and elem.val < curr_val:
            max_rank, max_elem = elem.rank, elem
    return max_elem


class Solution:
    def matrixRankTransform(self, matrix):

        soln = [[-math.inf for _ in row] for row in matrix]
        all_vals = collections.defaultdict(list)
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                all_vals[val].append((r, c))

        for curr_val in sorted(all_vals):

            # Build DSU
            uf = UnionFind()
            for r, c in all_vals[curr_val]:
                uf.make_set((r, c))
            for a, b in itertools.combinations(all_vals[curr_val], 2):
                if a[0] == b[0] or a[1] == b[1]:
                    # If the two values share a column or row, union.
                    uf.union_set(a, b)

            for r, c in all_vals[curr_val]:
                # First see if my DSU set has been ranked.
                if uf.has_rank((r, c)):
                    soln[r][c] = uf.get_rank((r, c))

                # Determine the value and position of the maximum value
                # that has been ranked in my row and col.
                max_elem = max_ranked(r, c, matrix, soln)

                if max_elem is None:
                    # If there are no values ranked yet, then I should
                    # have rank of 1.
                    soln[r][c] = 1
                elif max_elem.val == curr_val:
                    # If the max ranked element has the same value as me,
                    # then I should be the same value as it.
                    soln[r][c] = max_elem.rank
                else:
                    soln[r][c] = max_elem.rank + 1

                # I am now the max ranked element in my row and column.
                uf.set_rank((r, c), soln[r][c])

            for r, c in all_vals[curr_val]:
                # Set all the values to the maximum rank of their set.
                soln[r][c] = uf.get_rank((r, c))

        return soln



def test_1():
    matrix = [[1,2],[3,4]]
    expected = [[1,2],[2,3]]
    result = Solution().matrixRankTransform(matrix)
    print('expected')
    for row in expected:
        print(row)
    assert result == expected


def test_2():
    matrix = [[7,7],[7,7]]
    expected = [[1,1],[1,1]]
    result = Solution().matrixRankTransform(matrix)
    print('expected')
    for row in expected:
        print(row)
    assert result == expected


def test_3():
    matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
    expected = [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
    assert Solution().matrixRankTransform(matrix) == expected


def test_4():
    matrix = [[7,3,6],[1,4,5],[9,8,2]]
    expected = [[5,1,4],[1,2,3],[6,3,1]]
    assert Solution().matrixRankTransform(matrix) == expected


def test_5():
    matrix = [[-21, -10, 42, 25, 6, 16, 11, -22, -15, -37, -3, -9, 49, 34, -1, 50, 6, -49, 36, 23, -35, 19, -25, -18, -36], [-2, 15, -16, -42, -10, 8, 44, -49, 21, 42, 11, -27, 47, 41, 23, 0, 41, 5, 46, 28, 26, 9, 13, 15, 23], [-20, -22, -44, -2, 17, -30, 19, 37, -7, -14, 0, -43, 8, -41, 25, 22, -23, 35, 34, 36, 7, 27, 45, -8, 25], [-40, 1, 13, -9, 30, -18, -24, -43, -30, 47, -6, 30, 17, -36, -28, -43, 26, -45, 17, 5, -37, -12, 26, -30, 40], [43, -20, 12, -35, -21, 1, -47, 13, -30, 4, 29, -36, -7, 44, 35, 50, -11, 8, -1, -3, 40, -42, 30, 43, 10], [5, -12, -37, -20, 14, 35, 29, 21, -5, 49, 11, 4, -16, 42, -30, 31, 15, 24, -48, -1, -38, 32, 4, -10, -31], [36, 21, -6, -10, -44, 15, 41, -48, 18, 47, 17, -32, -13, -6, -30, -46, -3, -32, 47, -7, 21, -41, -15, 31, -12], [3, -43, 28, 18, -17, -32, 0, 44, 50, -36, 48, 10, 50, 0, -17, -38, -35, 15, 10, -21, -5, 29, -18, 17, 32], [-19, -42, 7, 30, -18, 6, 50, 45, 6, -35, -36, -18, -18, -24, -21, 7, -36, 34, -48, 17, -11, 8, -48, 12, -21], [-31, -17, -18, 10, -45, 17, -4, -10, 15, -20, -32, -40, -17, -42, -35, -10, -22, -37, 29, 8, 18, -44, -3, -10, 36], [-4, -42, 12, 49, -45, -37, 13, 38, 50, -48, 37, 15, -42, 37, 45, 31, 33, -16, 31, 9, -11, 16, -33, -34, -33], [-29, 4, -10, 50, 34, -12, 43, 27, 37, 35, -40, 46, 1, 8, -14, 22, 43, 29, 3, 10, -46, 34, -22, 30, 18], [18, 14, 24, 6, -12, -13, 31, 22, -28, 11, -37, -20, -9, -48, -30, 41, -18, 1, 46, 49, 31, 16, 5, 32, -21], [48, 34, 26, 50, 45, -23, -43, -46, -39, 36, 49, -16, -3, 49, 8, -48, 26, -25, -12, 44, 37, -23, -19, -48, 26], [43, -13, 16, -12, -14, 22, 46, -19, 7, 34, 38, -1, 39, -15, -50, -15, 40, 44, -18, 7, -23, -46, -7, -41, -42], [-20, -9, -26, -35, -34, 24, -25, 10, 22, -25, -50, -39, 44, 7, -29, 49, 5, 38, -33, -11, 35, -50, -11, -31, -30], [-7, 45, 4, 18, 50, 11, -39, 8, 33, -24, -28, 7, -50, 7, 30, 16, 1, 43, -29, -8, -48, 4, 38, -49, 5], [-16, 23, 16, 9, 40, -11, 50, 32, 42, -50, -9, 12, -35, -38, 14, 18, 19, -25, 31, 7, 14, 6, -25, 4, -26], [-26, -31, 2, 9, 34, 10, -45, 17, 4, 46, 24, -43, 24, -24, 15, -23, 16, -25, -15, 5, 39, -44, 8, -47, 33], [-32, -16, -45, -30, 11, 21, -22, 7, -45, 6, 48, 25, 36, -17, -40, -1, -46, -11, -19, 5, 43, -18, -20, -11, -24], [-43, 12, -6, 3, 45, -10, 5, 0, 22, 18, 9, -29, -29, 13, 14, 13, -13, 9, -23, -26, 3, 21, 16, -29, 32], [-19, -33, -42, -29, -12, 1, 19, 47, -14, -47, -39, -1, -20, 13, 15, 25, -50, -37, 17, 18, -47, -41, -8, -46, 49], [46, 34, 9, 36, -31, 40, -17, -28, -19, -26, 2, 24, 44, -6, 30, -19, 14, -11, 19, -16, 20, -49, -11, -3, -26], [-35, -10, 20, 17, 6, 11, -47, 22, 38, -15, -33, 16, 30, -18, 15, -46, 5, -45, 23, 14, 28, -49, 1, 24, 14], [15, -45, -2, 17, 10, -8, -6, 2, 36, 41, -39, -31, 30, 8, -4, 36, 24, 42, -37, -9, 5, 38, 43, -1, -19]]
    expected = [[19,29,51,45,35,41,36,18,21,5,32,30,60,46,33,61,35,1,50,44,9,43,17,20,6],[31,41,22,2,28,36,57,1,43,56,39,17,59,54,44,32,54,33,58,47,46,38,40,41,44],[20,16,4,32,41,14,44,52,31,22,33,7,37,8,46,45,15,50,49,51,36,47,58,30,46],[7,32,40,30,48,20,19,6,15,59,31,48,42,10,17,6,47,5,42,35,8,24,47,15,53],[58,17,39,11,16,33,3,40,15,34,45,10,29,59,49,61,23,35,32,31,57,7,48,58,36],[35,28,7,14,40,51,46,44,32,60,39,34,24,55,12,48,41,45,1,33,6,50,34,29,9],[50,45,31,29,5,40,51,2,42,59,41,11,25,31,12,4,32,11,59,30,45,8,24,49,26],[33,2,48,44,24,13,32,54,61,8,59,37,61,32,24,7,12,38,37,18,25,49,23,42,50],[21,4,36,46,22,35,61,55,35,12,11,22,22,18,19,36,11,48,1,41,23,37,1,38,19],[14,23,21,38,3,42,31,29,39,20,13,8,23,7,11,29,16,10,47,37,43,6,32,29,52],[30,4,39,55,3,5,40,53,61,2,50,41,4,50,54,48,49,18,48,38,23,42,8,7,8],[15,34,27,62,52,26,55,46,54,53,6,56,31,37,25,45,55,47,33,39,5,52,18,48,41],[43,38,46,36,27,22,49,45,16,37,10,20,28,1,12,51,21,29,58,59,49,42,35,50,19],[60,48,47,62,57,18,6,4,7,54,61,23,30,61,34,3,47,17,25,56,55,18,22,3,47],[58,27,41,28,26,44,60,19,36,45,51,31,52,25,1,25,53,59,23,36,10,3,29,6,4],[20,30,17,11,12,46,18,39,45,18,1,9,53,36,16,54,34,51,13,26,50,1,26,14,15],[29,58,34,44,59,39,7,38,48,19,15,36,1,36,47,40,33,57,14,28,3,34,49,2,35],[22,46,41,37,53,27,61,49,56,1,28,38,10,9,39,42,43,17,48,36,39,35,17,34,16],[16,12,33,37,52,38,5,43,34,57,44,7,44,18,41,19,42,17,24,35,56,6,36,4,51],[9,25,3,12,39,43,20,37,3,36,59,46,50,24,4,30,2,26,22,35,58,23,21,26,17],[1,37,31,33,57,28,34,32,45,42,36,16,16,38,39,38,22,36,18,17,33,44,41,16,50],[21,11,6,13,27,33,44,56,22,4,9,31,17,38,41,46,1,10,42,43,4,8,28,5,57],[59,48,37,49,13,52,21,14,20,16,34,45,53,31,47,20,38,26,43,22,44,2,26,32,16],[8,29,44,43,35,39,3,45,55,21,12,42,49,19,41,4,34,5,46,40,48,2,33,47,40],[39,1,32,43,38,29,30,34,50,55,9,12,49,37,31,50,44,56,10,27,35,53,57,33,20]]
    result = Solution().matrixRankTransform(matrix)
    print('expected')
    for row in expected:
        print(row)
    assert result == expected


def test_6():
    matrix = [[2, 4, 1, 5, -4, 3, -1, 2, 1, 3], [5, 0, 2, -1, -2, 4, 1, 5, -3, 1], [-1, 5, 5, 3, 4, -3, -4, -2, 3, -1], [5, -2, 1, 4, 1, 4, 5, 3, -4, 5], [-3, -4, 3, 0, 5, 1, 0, -2, 4, 2], [4, -4, -4, -5, -5, 3, 2, -4, -3, -3], [4, -5, -5, -5, -4, -2, 0, -2, 3, -1], [2, -3, 0, -3, -3, -5, 1, 5, 1, 0], [4, 4, 2, -5, 2, 2, 3, -2, -4, 4], [1, -5, 3, 3, 0, 0, 5, -1, 2, 5]]
    for row in matrix:
        print(row)
    expected = [[8,10,7,11,2,9,3,8,7,9],[11,6,8,5,4,10,7,11,3,7],[5,11,11,9,10,2,1,4,9,5],[11,4,7,10,7,10,11,9,2,11],[3,2,9,6,11,7,6,4,10,8],[10,2,2,1,1,9,8,2,3,3],[10,1,1,1,2,4,6,4,9,5],[8,3,6,3,3,1,7,11,7,6],[10,10,8,1,8,8,9,4,2,10],[7,1,9,9,6,6,11,5,8,11]]
    result = Solution().matrixRankTransform(matrix)
    print('expected')
    for row in expected:
        print(row)
    assert result == expected


def test_7():
    matrix = [[-5, 2, 0, -3, 0], [4, 2, 1, 5, -5], [-5, -3, 5, -5, 4], [-4, 2, 4, 0, -3], [1, -1, 0, -1, -3]]
    expected = [[1,7,5,2,5],[8,7,6,9,1],[1,2,9,1,6],[2,7,8,5,3],[6,4,5,4,3]]
    result = Solution().matrixRankTransform(matrix)
    print('expected')
    for row in expected:
        print(row)
    print('matrix')
    for row in matrix:
        print(row)
    assert result == expected
