"""
LeetCode :: November 2021 Challenge :: 1286. Iterator for Combination
jramaswami
"""


from typing import *


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.k = combinationLength
        self.n = len(self.characters)
        self.combo = list(range(self.k))
        left_limit = self.n - self.k
        self.limits = list(range(left_limit, left_limit + self.k))

    def _past_limit(self, i):
        return self.combo[i] > self.limits[i]

    def _increment(self):
        # Find the rightmost index that, when incremented, does not exceed
        # its limit.
        i = len(self.combo) - 1
        self.combo[i] += 1
        while i >= 0 and self._past_limit(i):
            i -= 1
            self.combo[i] += 1

        # All points past i must now be incremented to self.combo[j-1] + 1
        for j in range(i+1, len(self.combo)):
            self.combo[j] = self.combo[j-1] + 1

    def next(self) -> str:
        if not self._past_limit(0):
            S = "".join(self.characters[i] for i in self.combo)
            self._increment()
            return S

    def hasNext(self) -> bool:
        return not self._past_limit(0)


#
# Testing
#
import string
import random
import itertools


def test_1():
    itr = CombinationIterator("abc", 2)
    assert itr.next() == "ab"
    assert itr.hasNext() == True
    assert itr.next() == "ac"
    assert itr.hasNext() == True
    assert itr.next() == "bc"
    assert itr.hasNext() == False


def test_2():
    for _ in range(100):
        characters = sorted(random.sample(string.ascii_lowercase, 15))
        k = random.randint(1, len(characters))
        itr = CombinationIterator(characters, k)
        for combo in itertools.combinations(characters, k):
            s = "".join(combo)
            assert itr.hasNext()
            assert itr.next() == s

        assert itr.hasNext() == False
