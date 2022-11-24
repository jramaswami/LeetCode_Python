"""
LeetCode :: 79. Word Search
November 2022 Challenge
jramaswami
"""


class Solution:

    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def exist(self, board, word):

        def inbounds(r, c):
            "Return True if (r, c) is inside the board."
            return r >= 0 and r < len(board) and c >= 0 and c < len(board[r])

        def neighbors(r, c):
            "Return the neighbors of (r, c)"
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def dfs(r, c, i, visited):
            visited[r][c] = True
            if board[r][c] == word[i]:
                if i == len(word) - 1:
                    return True
                for r0, c0 in neighbors(r, c):
                    if not visited[r0][c0]:
                        if dfs(r0, c0, i+1, visited):
                            return True
            visited[r][c] = False
            return False

        visited = [[False for _ in row] for row in board]
        for r, row in enumerate(board):
            for c, _ in enumerate(row):
                if dfs(r, c, 0, visited):
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


def test_5():
    "TLE"
    board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A", "A","A"],["A","A","A","A","A","A"]]
    word = "AAAAAAAAAAAAAAB"
    expected = False
    assert Solution().exist(board, word) == expected