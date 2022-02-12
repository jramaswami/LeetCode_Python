"""
LeetCode :: 127. Word Ladder
"""


import string
import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        visited = {w: False for w in wordList}
        if endWord not in visited:
            return 0

        def neighbors(word):
            "Generator of the neighbors of the word."
            for i, c in enumerate(word):
                for q in string.ascii_lowercase:
                    if c == q:
                        continue
                    yield word[:i] + q + word[i+1:]

        # BFS
        queue = collections.deque()
        queue.append((beginWord, 1))
        visited[beginWord] = True
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for neighbor in neighbors(word):
                if neighbor not in visited:
                    continue
                if  not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
        return 0


def test_1():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    expected = 5
    assert Solution().ladderLength(beginWord, endWord, wordList) == expected


def test_2():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    expected = 0
    assert Solution().ladderLength(beginWord, endWord, wordList) == expected
