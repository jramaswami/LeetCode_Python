"""
LeetCode :: October 2021 Challenge :: 79. Word Search
jramaswami
"""


class Solution:

    def exist(self, board, word):

        def inbounds(r, c):
            """Return True if (r, c) is inside the board."""
            return r >= 0 and c >= 0 and r < len(board) and c < len(board[0])

        def neighbors(r, c):
            """Return the neighbors of (r, c)."""
            offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def dfs(r, c, i, visited):
            """DFS to see if the word is present."""
            if i >= len(word):
                return True

            if board[r][c] == word[i]:
                visited.add((r, c))
                for r0, c0 in neighbors(r, c):
                    if (r0, c0) not in visited and dfs(r0, c0, i+1, visited):
                        return True
                visited.remove((r, c))
            return False

        for r, row in enumerate(board):
            for c, _ in enumerate(row):
                if dfs(r, c, 0, set()):
                    return True
        return False


def test_1():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    expected = True
    assert Solution().exist(board, word) == expected


def test_2():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    expected = True
    assert Solution().exist(board, word) == expected


def test_3():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    expected = False
    assert Solution().exist(board, word) == expected


def test_4():
    """WA"""
    board = [["a"]]
    word = "a"
    expected = True
    assert Solution().exist(board, word) == expected
