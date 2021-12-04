"""
LeetCode :: December 2021 Challenge :: 1032. Stream of Characters
jramaswami
"""


import collections


class Search:

    def __init__(self, word):
        self.index = 0
        self.word = word

    def advance(self, letter):
        self.index += 1
        if self.index < len(self.word) and self.word[self.index] == letter:
            return True
        return False

    def done(self):
        return self.index == len(self.word) - 1

    def __repr__(self):
        return f"Search({self.word=} {self.index=}"


class StreamChecker:

    def __init__(self, words):
        self.words = set(words)
        self.active_searches = []
        self.letter_map = collections.defaultdict(list)
        for word in self.words:
            self.letter_map[word[0]].append(word)

    def query(self, letter):
        # First advance any active searches.
        next_searches = []
        result = False
        for search in self.active_searches:
            if search.advance(letter):
                next_searches.append(search)
                result = result or search.done()

        # Add any new search on first letter.
        for word in self.letter_map[letter]:
            search = Search(word)
            next_searches.append(search)
            result = result or search.done()

        self.active_searches = next_searches
        return result


def test_1():
    methods = ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
    arguments = [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
    expected = [None, False, False, False, True, False, True, False, False, False, False, False, True]

    checker = StreamChecker(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(checker, m)(*a) == e
