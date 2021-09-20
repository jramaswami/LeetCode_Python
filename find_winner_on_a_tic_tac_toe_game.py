"""
LeetCode :: September 2021 Challenge :: Find Winner on a Tic Tac Toe Game
jramaswami
"""


class Solution:

    def tictactoe(self, moves):

        def find_winner(grid):
            # Rows
            for row in grid:
                if all(c != ' ' and c == row[0] for c in row):
                    return True, row[0]
            # Columns
            for c, _ in enumerate(grid[0]):
                if all(grid[r][c] != ' ' and grid[r][c] == grid[0][c] for r, _ in enumerate(row)):
                    return True, grid[0][c]
            # Diagonals
            if all(grid[r][c] != ' ' and grid[r][c] == grid[0][0] for r, c in [(0, 0), (1, 1), (2, 2)]):
                return True, grid[0][0]
            if all(grid[r][c] != ' ' and grid[r][c] == grid[0][2] for r, c in [(0, 2), (1, 1), (2, 0)]):
                return True, grid[0][2]
            # No winner
            return False, ""

        def no_moves(grid):
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == " ":
                        return False
            return True

        grid = [[" " for _ in range(3)] for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            player = "A"
            if i % 2:
                player = "B"
            grid[r][c] = player

        winner_exists, winning_player = find_winner(grid)
        if winner_exists:
            return winning_player
        if no_moves(grid):
            return "Draw"
        return "Pending"


def test_1():
    moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    expected = "A"
    assert Solution().tictactoe(moves) == expected


def test_2():
    moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    expected = "B"
    assert Solution().tictactoe(moves) == expected


def test_3():
    moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    expected = "Draw"
    assert Solution().tictactoe(moves) == expected


def test_4():
    moves = [[0,0],[1,1]]
    expected = "Pending"
    assert Solution().tictactoe(moves) == expected
