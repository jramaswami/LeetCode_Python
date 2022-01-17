"""
LeetCode :: 127. Word Ladder
"""
from typing import *
from collections import defaultdict

class Node:
    def __init__(self, val = None):
        self.val = val
        self.children = [None for _ in range(26)]

    def add(self, index, word):
        if index >= len(word):
            self.val = word
            return

        child_index = ord(word[index]) - ord('a')
        if self.children[child_index] is None:
            self.children[child_index] = Node(word[index])
        self.children[child_index].add(index + 1, word)

    def find(self, index, word, acc):
        if acc > 1:
            return []

        if index >= len(word):
            return [self.val]

        found = []
        for child in (c for c in self.children if c):
            if child.val != word[index]:
                found.extend(child.find(index + 1, word, acc + 1))
            else:
                found.extend(child.find(index + 1, word, acc))
        return found


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        head = Node()
        for word in wordList:
            head.add(0, word, )

        print(head.find(0, beginWord, 0))


def test_1():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    assert Solution().ladderLength(beginWord, endWord, wordList) == 5
