"""
LeetCode :: July 2021 Challenge :: Reshape the Matrix
jramaswami
"""


class Solution:
    def matrixReshape(self, matrix, new_height, new_width):
        # Verify reshape is valid
        if len(matrix) * len(matrix[0]) != new_height * new_width:
            return matrix

        # Create new matrix
        new_matrix = [[0 for _ in range(new_width)] for _ in range(new_height)]

        for old_row_index, row in enumerate(matrix):
            for old_col_index, value in enumerate(row):
                # Convert old row and col indexes into a one dimensional index
                one_d_index = (old_row_index * len(matrix[0])) + old_col_index
                # Convert the one dimensional index into the new row and col indexes
                new_row_index = one_d_index // new_width
                new_col_index = one_d_index % new_width
                new_matrix[new_row_index][new_col_index] = value
        return new_matrix


def test_1():
    matrix = [[1,2],[3,4]]
    r= 1
    c = 4
    expected = [[1,2,3,4]]
    assert Solution().matrixReshape(matrix, r, c) == expected


def test_2():
    matrix = [[1,2],[3,4]]
    r = 2
    c = 4
    expected = [[1,2],[3,4]]
    assert Solution().matrixReshape(matrix, r, c) == expected
