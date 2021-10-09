"""
LeetCode :: October 2021 Challenge :: 212. Word Search II
jramaswami
"""


class TrieNode:

    def __init__(self):
        self.value = ""
        self.end_word = -1
        self.children = [None for _ in range(26)]

    def get_child(self, char):
        return self.children[ord(char) - ord('a')]

    def insert_child(self, char):
        self.children[ord(char) - ord('a')] = TrieNode()



class Solver:

    OFFSETS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, board, words):
        self.board = board
        self.visited = [[False for _ in row] for row in board]
        self.root = TrieNode()
        self.words = words
        self.found = [False for _ in self.words]
        for index, word in enumerate(self.words):
            self._insert(index, word)


    def _insert(self, index, word):
        """Insert word."""
        curr = self.root
        for c in word:
            if not curr.get_child(c):
                curr.insert_child(c)
            curr = curr.get_child(c)
        curr.end_word = index

    def _inbounds(self, r, c):
        """Return True if (r, c) is inside the board."""
        return r >= 0 and c >= 0 and r < len(self.board) and c < len(self.board[0])

    def _neighbors(self, r, c):
        """Return the 4 adjacent neighbors of (r, c)."""
        for dr, dc in Solver.OFFSETS:
            r0, c0 = r + dr, c + dc
            if self._inbounds(r0, c0):
                yield r0, c0

    def _search(self, r, c, curr_node):
        """DFS search of grid to find words using Trie."""

        if curr_node is None:
            return

        if curr_node.end_word >= 0:
            self.found[curr_node.end_word] = True

        self.visited[r][c] = True
        for r0, c0 in self._neighbors(r, c):
            if not self.visited[r0][c0]:
                next_node = curr_node.get_child(self.board[r0][c0])
                if next_node:
                    self._search(r0, c0, next_node)
        self.visited[r][c] = False

    def solve(self):
        """Solve problem."""
        for r, row in enumerate(self.board):
            for c, char in enumerate(row):
                first_node = self.root.get_child(char)
                if first_node:
                    self._search(r, c, first_node)
        return [wd for wd, fnd in zip(self.words, self.found) if fnd]


class Solution:
    def findWords(self, board, words):
        solver = Solver(board, words)
        return solver.solve()


def test_1():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    expected = ["eat","oath"]
    assert sorted(Solution().findWords(board, words)) == sorted(expected)


def test_2():
    board = [["a","b"],["c","d"]]
    words = ["abcb"]
    expected = []
    assert sorted(Solution().findWords(board, words)) == sorted(expected)


def test_3():
    """TLE"""
    board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
    words = ["lllllll","fffffff","ssss","s","rr","xxxx","ttt","eee","ppppppp","iiiiiiiii","xxxxxxxxxx","pppppp","xxxxxx","yy","jj","ccc","zzz","ffffffff","r","mmmmmmmmm","tttttttt","mm","ttttt","qqqqqqqqqq","z","aaaaaaaa","nnnnnnnnn","v","g","ddddddd","eeeeeeeee","aaaaaaa","ee","n","kkkkkkkkk","ff","qq","vvvvv","kkkk","e","nnn","ooo","kkkkk","o","ooooooo","jjj","lll","ssssssss","mmmm","qqqqq","gggggg","rrrrrrrrrr","iiii","bbbbbbbbb","aaaaaa","hhhh","qqq","zzzzzzzzz","xxxxxxxxx","ww","iiiiiii","pp","vvvvvvvvvv","eeeee","nnnnnnn","nnnnnn","nn","nnnnnnnn","wwwwwwww","vvvvvvvv","fffffffff","aaa","p","ddd","ppppppppp","fffff","aaaaaaaaa","oooooooo","jjjj","xxx","zz","hhhhh","uuuuu","f","ddddddddd","zzzzzz","cccccc","kkkkkk","bbbbbbbb","hhhhhhhhhh","uuuuuuu","cccccccccc","jjjjj","gg","ppp","ccccccccc","rrrrrr","c","cccccccc","yyyyy","uuuu","jjjjjjjj","bb","hhh","l","u","yyyyyy","vvv","mmm","ffffff","eeeeeee","qqqqqqq","zzzzzzzzzz","ggg","zzzzzzz","dddddddddd","jjjjjjj","bbbbb","ttttttt","dddddddd","wwwwwww","vvvvvv","iii","ttttttttt","ggggggg","xx","oooooo","cc","rrrr","qqqq","sssssss","oooo","lllllllll","ii","tttttttttt","uuuuuu","kkkkkkkk","wwwwwwwwww","pppppppppp","uuuuuuuu","yyyyyyy","cccc","ggggg","ddddd","llllllllll","tttt","pppppppp","rrrrrrr","nnnn","x","yyy","iiiiiiiiii","iiiiii","llll","nnnnnnnnnn","aaaaaaaaaa","eeeeeeeeee","m","uuu","rrrrrrrr","h","b","vvvvvvv","ll","vv","mmmmmmm","zzzzz","uu","ccccccc","xxxxxxx","ss","eeeeeeee","llllllll","eeee","y","ppppp","qqqqqq","mmmmmm","gggg","yyyyyyyyy","jjjjjj","rrrrr","a","bbbb","ssssss","sss","ooooo","ffffffffff","kkk","xxxxxxxx","wwwwwwwww","w","iiiiiiii","ffff","dddddd","bbbbbb","uuuuuuuuu","kkkkkkk","gggggggggg","qqqqqqqq","vvvvvvvvv","bbbbbbbbbb","nnnnn","tt","wwww","iiiii","hhhhhhh","zzzzzzzz","ssssssssss","j","fff","bbbbbbb","aaaa","mmmmmmmmmm","jjjjjjjjjj","sssss","yyyyyyyy","hh","q","rrrrrrrrr","mmmmmmmm","wwwww","www","rrr","lllll","uuuuuuuuuu","oo","jjjjjjjjj","dddd","pppp","hhhhhhhhh","kk","gggggggg","xxxxx","vvvv","d","qqqqqqqqq","dd","ggggggggg","t","yyyy","bbb","yyyyyyyyyy","tttttt","ccccc","aa","eeeeee","llllll","kkkkkkkkkk","sssssssss","i","hhhhhh","oooooooooo","wwwwww","ooooooooo","zzzz","k","hhhhhhhh","aaaaa","mmmmm"]
    expected = []
    assert sorted(Solution().findWords(board, words)) == sorted(expected)
