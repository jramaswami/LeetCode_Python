"""
LeetCode :: May 2021 Challenge :: Search Suggestion System
jramaswami
"""


from typing import *
from bisect import insort


class TrieNode:

    def __init__(self, char=None, index=None):
        self.children = dict()
        self.suggestions = []
        self.char = char
        self.index = index

    def add_word(self, word):
        self._add_word(word, -1)

    def _add_word(self, word, index):
        if self.index is not None:
            insort(self.suggestions, word)
            while len(self.suggestions) > 3:
                self.suggestions.pop()
        if index + 1 < len(word):
            char = word[index + 1]
            if char not in self.children:
                self.children[char] = TrieNode(char, index + 1)
            self.children[char]._add_word(word, index + 1)

    def search_word(self, word):
        acc = []
        self._search_word(word, -1, acc)
        return acc

    def _search_word(self, word, index, acc):
        if self.index is not None:
            acc.append(list(self.suggestions))
        if index + 1 < len(word):
            char = word[index + 1]
            if char not in self.children:
                for _ in range(index + 1, len(word)):
                    acc.append([])
                return acc
            self.children[char]._search_word(word, index + 1, acc)

    def __repr__(self):
        return f"TrieNode({self.index=} {self.char=} {self.suggestions=} {self.children=}"


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = TrieNode()
        for word in products:
            trie.add_word(word)
        soln = trie.search_word(searchWord)
        return soln


def test_1():
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    expected = [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]
    assert Solution().suggestedProducts(products, searchWord) == expected


def test_2():
    products = products = ["havana"]
    searchWord = "havana"
    expected = [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    assert Solution().suggestedProducts(products, searchWord) == expected


def test_3():
    products = ["bags","baggage","banner","box","cloths"]
    searchWord = "bags"
    expected = [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
    assert Solution().suggestedProducts(products, searchWord) == expected


def test_4():
    products = ["havana"]
    searchWord = "tatiana"
    expected = [[],[],[],[],[],[],[]]
    assert Solution().suggestedProducts(products, searchWord) == expected


def test_5():
    products = ["abcdef", "abcefg", "abcfgh", "abcghi"]
    searchWord = "abcxyz"
    expected = [["abcdef", "abcefg", "abcfgh"], ["abcdef", "abcefg", "abcfgh"], ["abcdef", "abcefg", "abcfgh"],
                [], [], []]
    assert Solution().suggestedProducts(products, searchWord) == expected