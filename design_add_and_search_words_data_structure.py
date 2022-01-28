"""
LeetCode :: January 2022 Challenge :: 211. Design Add and Search Words Data Structure
jramaswami
"""


class TrieNode:

    def __init__(self):
        self.children = dict()
        self.is_word = False

    def add_letter(self, letter):
        if letter not in self.children:
            self.children[letter] = TrieNode()
        return self.children[letter]

    def get_letters(self, letter):
        if letter == '.':
            for child in self.children:
                yield self.children[child]
        elif letter in self.children:
            yield self.children[letter]
        else:
            yield None

    def end_word(self):
        self.is_word = True


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for c in word:
            curr = curr.add_letter(c)
        curr.end_word()

    def find_word(self, word):
        return self._find_word(self.root, 0, word)

    def _find_word(self, curr, index, word):
        # Handle non-existent character.
        if curr is None:
            return False

        # Handle end of word.
        if index == len(word):
            return curr.is_word

        return any(
            self._find_word(child, index + 1, word) for child in curr.get_letters(word[index])
        )


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.add_word(word)

    def search(self, word):
        return self.trie.find_word(word)


def test_1():
    methods = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    arguments = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    expected = [None,None,None,None,False,True,True,True]

    wd = WordDictionary()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(wd, m)(*a) == e
