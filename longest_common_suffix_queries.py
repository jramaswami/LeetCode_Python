"""
LeetCode
3093. Longest Common Suffix Queries
May 2026 Challenge
jramaswami
"""


from typing import List


INF = pow(10, 10)


class TrieNode:
    def __init__(self, char, index, length):
        self.char = char
        self.children = {}
        self.index = index
        self.length = length


def add(root, word, index):
    word0 = word[::-1]
    node = root
    for char in word0:
        if char not in node.children:
            node.children[char] = TrieNode(char, index, len(word))
        node = node.children[char]
        if len(word) < node.length:
            node.index = index
            node.length = len(word)


def find_longest_suffix(root, word):
    word0 = word[::-1]
    result = root.index
    node = root
    for char in word0:
        if char not in node.children:
            return result
        result = node.children[char].index
        node = node.children[char]
    return result


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode('', INF, INF)
        for i, word in enumerate(wordsContainer):
            add(root, word, i)
            if len(word) < root.length:
                root.index = i
                root.length = len(word)
        soln = []
        for word in wordsQuery:
            soln.append(find_longest_suffix(root, word))
        return soln


def test_1():
    wordsContainer = ["abcd","bcd","xbcd"]
    wordsQuery = ["cd","bcd","xyz"]
    expected = [1,1,1]
    assert Solution().stringIndices(wordsContainer, wordsQuery) == expected


def test_2():
    wordsContainer = ["abcdefgh","poiuygh","ghghgh"]
    wordsQuery = ["gh","acbfgh","acbfegh"]
    expected = [2,0,2]
    assert Solution().stringIndices(wordsContainer, wordsQuery) == expected